'''
file: MyMovieExplorer/query4.py
ZhaoXiang Lan, 12/10/2025

description:
keep the top 10 movies with rantings or revenue
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
from algorithms.heapsort import MinHeap
from DataStructures.array import array

class Top10_Movies:
    # constructor
    def __init__(self):
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
                    for g in parsed:
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
    
    # function to get top 10 movies ratings or revenue value 
    def get_top10_movies(self, movie, key):
        # get the value by key
        value = movie.get(key, 0)

        # handle missing or invalid values
        if value is None:
            return 0
        
        s = str(value).strip().lower()
        if s == "" or s == "nan":
            return 0

        try:
            # convert value to float
            return float(value)
        except:
            return 0
    
    def top10_update(self, heap, movie_index, key, k):
        # get the movie and its value
        movie = self.movies_array.get(movie_index)
        # get the value by key
        new_val = self.get_top10_movies(movie, key)

        # if heap is not full yet, just push
        if heap.size() < k:
            heap.push((new_val, movie))
            return

        # if heap is full, compare with the smallest in heap
        smallest_pair = heap.peek()
        if smallest_pair is None:
            return

        smallest_val = smallest_pair[0]

        # if new movie is better, replace the smallest one
        if new_val > smallest_val:
            heap.pop()
            heap.push((new_val, movie))
        
    # compute top-10 by a given key using a min-heap
    def top_10_by_key(self, key, size = 10):
        # create a min-heap to store the top 10 movies
        heap = MinHeap()

        # scan all movies
        for i in range(self.movies_array.size()):
            self.top10_update(heap, movie_index=i , key=key, k=size)

        # return the top 10 movies in ascending order
        pairs_asc = heap.get_all_elements()

        # reverse the order to get descending order
        pairs_desc = array()

        index = pairs_asc.size() - 1

        while index >= 0:
            pair = pairs_asc.get(index)   # (score, movie)
            if pair is not None:  # add null check
                movie = pair[1]
                pairs_desc.append(movie)
            index -= 1

        # return the result array
        return pairs_desc

    # display the top 10 movies
    def display(self, top_10_movie, key):
        # header
        print(f"Top 10 movies by {key}:")
        print("\n" + "=" * 40)
        print(f"Top {top_10_movie.size()} movies by {key}")
        print("=" * 40)
        
        # display each movie
        index = 0
        rank = 1

        while index < top_10_movie.size():
            movie = top_10_movie.get(index)

            # Title
            title = movie.get("title")
            if not title:
                title = movie.get("original_title")
            if not title:
                title = "Unknown Title"
            # Key value
            value = self.get_top10_movies(movie, key)
            # Release date
            if "release_date" in movie:
                release_date = movie["release_date"]
            else:
                release_date = "Unknown"

            # print the movie info
            print(f"\n#{rank}: {title}")
            print(f"{key}: {value}")
            print(f"Release date: {release_date}")
            # increment counters
            rank += 1
            index += 1

        print("\n" + "=" * 40 + "\n")