import os 
import imdb_scrapper
import sys

#specify folder path with movies here or in argument
path = os.chdir("/Users/Arslan/Movies/test")

def rename_all_in_path(path):
    for file in os.listdir(path):
        filename, file_extension = os.path.splitext(file)
        
        if filename[0]!=".": #skip hidden files
            try:
                movie=imdb_scrapper.get_result(filename) 
                #(title,year,rating,votes,time.strip(),maturity_rating.strip(),genre,summary)
                new_name=movie[0]+" ["+movie[1]+"] "+movie[2]+" ("+movie[3]+") "+str(movie[6])+file_extension
                filename=filename.replace('.',' ')
                filename=filename.replace('-',' ')
                print(filename.split()[0])
                print(movie[0].split()[0]) 
                if filename.split()[0]==movie[0].split()[0]: #Dont change name if picked wrong urlfrom imdb
                    print("\nChanging name ...")
                    print(file," ---> ",new_name)
                    print(type(new_name))
                    os.rename(file, new_name)
            except:
                print("keeping original name for ",file)

#python rename_files.py "/Users/Arslan/Movies/test" 
if __name__ == '__main__':
    try:
        rename_all_in_path(os.chdir(sys.argv[1]))
    except:
        rename_all_in_path(path)
