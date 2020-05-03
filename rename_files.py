import os 
import imdb_scrapper
import sys

#specify folder path with movies here or in argument
path = os.chdir("/Users/Arslan/Movies/test") #default path for me if not set in argument. Change it to your own

def rename_all_in_path(path):
    """
    renamed all movies in given path

    Parameters:
    path (str): "/Users/Arslan/Movies/test" 

    Returns:
    renamed files in the given path

    Future:
    
    """
    
    for file in os.listdir(path):
        filename, file_extension = os.path.splitext(file)
        
        if filename[0]!=".": #skip hidden files
            try:
                movie=imdb_scrapper.get_result(filename) 
                #(title,year,rating,votes,time.strip(),maturity_rating.strip(),genre,summary)
                new_name=movie[0]+" ["+movie[1]+"] "+movie[2]+" ("+movie[3]+") "+str(movie[6])+file_extension
                filename=filename.replace('.',' ')
                filename=filename.replace('-',' ')
                if filename.split()[0]==movie[0].split()[0]: #Dont change name if picked wrong urlfrom imdb
                    print("\nChanging name ...")
                    print(file," ---> ",new_name)
                    print(type(new_name))
                    os.rename(file, new_name)
            except:
                print("keeping original name for ",file)

#python rename_files.py "/Users/Arslan/Movies/test" 
if __name__ == '__main__':
    """
    e.g.

    python rename_files.py "/Users/Arslan/Movies/test" 

    should convert file in 'test/Burn.After.Reading.XYb.83832.msaniu.mp4' to
    'test/Burn After Reading [2008] 7.0(298,973) ['Comedy', 'Crime', 'Drama'].mp4'

    """
    try:
        rename_all_in_path(os.chdir(sys.argv[1]))
    except:
        rename_all_in_path(path)
