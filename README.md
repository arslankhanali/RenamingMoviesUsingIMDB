# Have a folder with messy movie names?
# Problem Solved!

## Requirments:
 - pip3 install virtualenv
 - virtualenv venv
 - source venv/bin/activate
 - pip3 install -r requirements.txt

## Run
```yml
python rename_files.py <path of your folder>
```

## Has some other very useful function 

```yml
def get_movie_information(full_movie_url):
    """
    Extracts information from the link of a movie's imdb page

    Parameters:
    full_movie_url (str): link of a movie's imdb page

    Returns:
    tuple:(title,year,rating,votes,time.strip(),maturity_rating.strip()
    ,genre,summary)

    Future:
    Try to extract more inforamtion and more efficiently
    """

``` 
```python
def clean_movie_name(name):
    """
    Parses raw movie names to make searchable movie name for imdb

    Parameters:
    name(str): raw name

    Returns:
    str:searchable movie name for imdb

    Future:
    Make more robust 
    Cater alot more edge cases
    """
``` 
```java
def find_movie_url(name):
    """
    find imdb url from the movies name

    Parameters:
    name(str): cleaned up name

    Returns:
    str:url

    Future:
    Right now only works if we sucessfully find a movie
    Picks the first movie only
    """
``` 
```python
def get_result(raw_name):
    """
    end to end function. gets information from raw name

    Parameters:
    raw name(str): original file name

    Returns:
    str: information of a movie from imdb, used to rename the file accordingly 

    Future:
    
    """
``` 
```java
def rename_all_in_path(path):
    """
    renamed all movies in given path

    Parameters:
    path (str): "/Users/Arslan/Movies/test" 

    Returns:
    renamed files in the given path

    Future:
    
    """
``` 

## Tested and written on mac os

Please fork and add more features.\
Cheers\
RC