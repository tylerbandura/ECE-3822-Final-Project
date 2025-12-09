'''
file: MyMovieExplorer/query1.py
ZhaoXiang Lan, 12/8/2025

description:
the program to find a movie by title
'''
# input the root path
import os
import sys

# add the project root to sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# inport necessary modules
import pandas as pd
import ast
from DataStructures.array import array, BucketArray
from DataStructures.hashTable import HashTable

class Find_Movie_By_Title:
    def __init__(self):
        self.movie_title_table = None
        self.movies_array = None
    
    # function to load movies from csv file
    def load_movies_from_csv(self, file_path):
        # read movie data from csv file using pandas
        df = pd.read_csv(file_path)

        # convert dataframe to list of dictionaries
        movies = df.to_dict(orient='records')

        # create a dynamic array to hold the movies
        array_of_movies = array()

        # append each movie to the dynamic array
        for movie in movies:
            # parse the genres field from string to list of dictionaries
            genres_str = movie.get('genres')

            if isinstance(genres_str, str) and genres_str.strip():
                try:
                    parsed = ast.literal_eval(genres_str)
                    genre_array = array()
                    for g in parsed:                    # convert list → array()
                        genre_array.append(g)
                    movie["genres"] = genre_array
                except:
                    movie["genres"] = array()
            else:
                movie["genres"] = array() 

            array_of_movies.append(movie)
        
        # store the movies array
        self.movies_array = array_of_movies

        # return the dynamic array of movies 
        return array_of_movies

    # build the hashtable indexed by movie titles
    def build_title_hashtable(self, movies_array):

        # build the hashtable with larger size to reduce collisions
        movie_title_table = HashTable(size=100000)

        # iterate through the movies array
        for movie in range(movies_array.size()):

            # get the movie data
            movie_data = movies_array.get(movie)

            # get the title
            title = movie_data['title'].strip().lower() # added this to fix case sensitivity

            # insert into the hashtable using title as key
            movie_title_table.insert(title, movie_data)

        # store the hashtable
        self.movie_title_table = movie_title_table

        # return the table
        return movie_title_table

    # function to lookup a movie by title
    def find_movie_by_title(self, movie_title_table, title):
        # lookup the movie in the hashtable
        movie = movie_title_table.lookup(title.strip().lower()) # added to fix case sensitivity

        # return the movie data
        return movie
    
    # display movie information
    def display_movie_info(self, movie):
        if movie:
            print("\nMovie found!")
            print("------------------------------")
            print("Title:", movie["title"])
            print("Release Date:", movie["release_date"])
            print("Budget:", movie["budget"])
            print("Revenue:", movie["revenue"])
            
            # Extract only genre names from the genres array
            genres_array = movie["genres"]
            genre_names = []
        
            # Iterate through the genres array to extract names
            for i in range(genres_array.size()):
                genre_dict = genres_array.get(i)
                if isinstance(genre_dict, dict) and 'name' in genre_dict:
                    genre_names.append(genre_dict['name'])
        
            # Display genres as a clean comma-separated list
            if genre_names:
                print("Genres:", ', '.join(genre_names))
            else:
                print("Genres: None")
        else:
            print("\nMovie not found.")