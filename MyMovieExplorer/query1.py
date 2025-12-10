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
from matplotlib.pyplot import title
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
            # check if genres_str is a valid string before parsing
            if isinstance(genres_str, str) and genres_str.strip():
                try:
                    # use ast.literal_eval to safely parse the string representation of a list
                    parsed = ast.literal_eval(genres_str)
                    # convert the parsed list to a dynamic array
                    genre_array = array()
                    # append each genre dictionary to the dynamic array
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

        # If movie is None, stop immediately
        if not movie:
            print("\nMovie not found.")
            return

        print("\n" + "-" * 40)

        # Title
        title = movie.get("title")
        if not title:
            title = movie.get("original_title")
        if not title:
            title = "Unknown Title"
        
        print(f"Title: {title}")

        # Release Year
        release_date = movie.get("release_date", "")

        if len(release_date) >= 4:
            year = release_date[:4]
        else:
            year = "Unknown"

        # Runtime
        runtime = movie.get("runtime")
        if runtime:
            # Convert safely in case runtime is a string like "81.0"
            runtime = int(float(runtime))
            hours = runtime // 60
            minutes = runtime % 60
        
            runtime_str = f"{hours}h {minutes}m"
        else:
            runtime_str = "Unknown"

        # Language
        # Convert language code to uppercase
        lang = movie.get("original_language", "Unknown")
        if isinstance(lang, str):
            lang = lang.upper()
        else:
            lang = "UNKNOWN"

        # Print year, runtime, and language in one line
        print(f"{year} | {runtime_str} | {lang}")

        # Tagline
        # CSV data often contains "nan" as a string for missing values
        # skip those to avoid ugly output.
        tagline = movie.get("tagline")
        if tagline and str(tagline).lower() != "nan":
            print(f"Tagline: {tagline}")

        # Genres
        # Get the "genres" field from the movie dictionary
        genres_array = movie.get("genres")

        # A list to store the names of genres
        genre_names = []

        # First: make sure genres_array is your custom array type
        if genres_array:
            has_size = hasattr(genres_array, "size")
            has_get = hasattr(genres_array, "get")

            if has_size and has_get:
                # Loop through the array using a simple counter
                index = 0
                total_items = genres_array.size()

                while index < total_items:
                # Get the element at current index
                    item = genres_array.get(index)

                    # Each element should be a dictionary like {"id": x, "name": y}
                    if isinstance(item, dict):
                        if "name" in item:
                            genre_names.append(item["name"])

                    # Move to next index
                    index += 1
                    
        # genre_names contains all the genre names
        # print them as a comma-separated string
        if len(genre_names) > 0:
            genres_text = ", ".join(genre_names)
            print("Genres: " + genres_text)
        
        # Budget
        # Convert to int if possible for nice formatting
        budget_value = movie.get("budget")

        if budget_value:
            try:
                budget_float = float(budget_value)
                budget_int = int(budget_float)
                budget_string = f"${budget_int:,}"
                print("Budget: " + budget_string)
            except:
                print("Budget: " + str(budget_value))
        
        # Revenue
        revenue_value = movie.get("revenue")

        if revenue_value:
            try:
                revenue_float = float(revenue_value)
                revenue_int = int(revenue_float)
                revenue_string = f"${revenue_int:,}"
                print("Revenue: " + revenue_string)
            except:
                print("Revenue: " + str(revenue_value))

        # Rating
        vote_average = movie.get("vote_average")
        if vote_average is not None:
            print("Rating: " + str(vote_average) + " / 10 stars")

        vote_count = movie.get("vote_count")
        if vote_count:
            print("Total Votes: " + str(vote_count))

        # Overview / Synopsis
        overview = movie.get("overview")

        if overview:
            overview_lower = str(overview).lower()
            # skip "nan" strings to avoid ugly output.
            if overview_lower != "nan":
                print("Synopsis: " + str(overview))

        print("-" * 40 + "\n")