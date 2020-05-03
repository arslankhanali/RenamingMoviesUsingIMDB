import os 
import imdb_scrapper

path = os.chdir("/Users/Arslan/Movies/test")

def rename_all_in_path(path):
    for file in os.listdir(path):
        filename, file_extension = os.path.splitext(file)
        print(filename)
        print(file_extension)

        try:
            movie=imdb_scrapper.get_result(filename) 
            #(title,year,rating,votes,time.strip(),maturity_rating.strip(),genre,summary)
            new_name=movie[0]+" ["+movie[1]+"] "+movie[2]+"("+movie[3]+") "+str(movie[6])+file_extension
            print(file," = ",new_name)
            print(type(new_name))
            os.rename(file, new_name)
        except:
            print("keeping original name for ",file)

if __name__ == '__main__':
    
    rename_all_in_path(path)
