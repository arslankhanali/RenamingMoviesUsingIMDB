import sys
import requests
from bs4 import BeautifulSoup
import re
import math

def get_movie_information(full_movie_url):
    response = requests.get(full_movie_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #get rating
    rating= (soup.find("span", itemprop="ratingValue").text)
    #get year
    year= (soup.find("span", id="titleYear").text[1:-1])
    #get title
    temp_s=soup.h1.text
    i=temp_s.find("\xa0")
    title=temp_s[:i]
    #runtime
    time=soup.find('time').text
    #get maturity rating
    temp= soup.find("div", {"class": "subtext"})
    for i in temp:
        maturity_rating=i
        maturity_rating.strip()
        break
    #get genre
    genre_releasedate=[i.text for i in temp.findAll('a')]
    genre=genre_releasedate[:-1]
    #get releasedate in Your country
    release_date=genre_releasedate[-1]
    #total votes
    votes=(soup.find("span", itemprop="ratingCount").text)
    #get summary
    summary=soup.find("div", class_="summary_text").text.strip()

    return (title,year,rating,votes,time.strip(),maturity_rating.strip()
    ,genre,summary)

def clean_movie_name(name):
    flag=1
    #replace . with white spaces
    name=name.replace('.',' ')
    name=name.replace('-',' ')
    #take everything before date
    for i in range(len(name)-4):
        if name[i:i+4].isdigit():
            name = name[:i]
            flag=0
            break
    #if there is no date than take everything if len<=4
    # Otherwise take half of remaining name   
    if flag!=0:
        words=name.split()
        l=len(words)
        if l>4:
            words=words[:math.floor(l-l/2)]
    name=(re.sub("[^A-Za-z0-9\s]+", "", name)) #remove special characters except whitespaces 
    
    return name

def find_movie_url(name):
    response = requests.get('https://www.imdb.com/find?q='+name)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    try:
        return "https://www.imdb.com"+soup.find("td", class_="result_text").a.get('href')
    except:
        return None

def get_result(raw_name):
    while True:
        try:
            clean_name=clean_movie_name(raw_name)
            print("Clean name is: ", clean_name,"\n")
        except:
            print("Cloud not clean ", raw_name,"\n")
            break
            

        try:
            movie_url_of_imdb=find_movie_url(clean_name)
            print("imdb url for ", clean_name," is ",movie_url_of_imdb,"\n")
        except:
            print("Cloud not find imdb url for ", clean_name,"\n")
            break
            

        try:
            result=get_movie_information(movie_url_of_imdb)
            print("Movie information:", result)
            return (result)
        except:
            print("Cloud not parse movie information for ",clean_name," ",movie_url_of_imdb,"\n")
            break
            
#python imdb_scrapper.py "matrix#^%&* reload100000000ed"            
if __name__ == '__main__':
    print(sys.argv[1]) 
    get_result(sys.argv[1])