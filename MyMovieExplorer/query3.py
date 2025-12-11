import os
import sys
from DataStructures.bst import BST
import pandas as pd
import ast

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from DataStructures.array import array


class Movie:
    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year

class FindMoviesByGenre:
    def __init__ (self):
        self.root = None

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

    def build_year_bst(self, movies_array):
        # Create a new BST that will store movies by their release year
        year_bst = BST()

        # Use index-based loop because our custom array is not iterable
        index = 0
        total = movies_array.size()   # use your array.size() method
        while index < total:
            # Get the movie at the current index
            movie = movies_array.get(index)

            # Safely get the release year from the movie dict
            release_date = movie.get("release_date")
            # Check if release_date is not None and not NaN (pd.isna check)
            if release_date is not None and str(release_date) != 'nan' and len(str(release_date)) >= 4:
                year_str = str(release_date)[:4]

                try:
                    year = int(year_str)
                    # Insert this movie into the BST under this year
                    year_bst.insert(year, movie)
                except ValueError:
                    # If the year is not a valid number, just skip this movie
                    pass
            # Move to the next index
            index += 1

        return year_bst

    
    def find_movies_by_genre_in_two_given_year(self, year_bst, genre,start_year, end_year):
        result = array()
        self._inorder_traversal(year_bst.root, genre, start_year, end_year, result)
        return result
    
    def _inorder_traversal(self, node, genre, start_year, end_year, result):
        # Base case: if the node is empty, do nothing
        if node is None:
            return

        # 1. Traverse left subtree
        self._inorder_traversal(node.left, genre, start_year, end_year, result)
        # 2. Process current node if its year is in the given range
        if start_year <= node.node_year <= end_year:

            # node.node_movies is our custom array, so we use index-based loop
            index = 0
            total = node.node_movies.size()

            while index < total:
                # movie is a dictionary (from pandas)
                movie = node.node_movies.get(index)

                # Get the genres array stored in the movie dictionary
                genres_array = movie.get("genres")
                # Flag to tell if this movie matches the target genre
                has_genre = False

                # Check that genres_array is our custom array type
                if genres_array and hasattr(genres_array, "size") and hasattr(genres_array, "get"):
                    j = 0
                    count = genres_array.size()

                    # Loop over each genre entry
                    while j < count:
                        g = genres_array.get(j)

                        # We expect g to be something like {"id": ..., "name": "Animation"}
                        if isinstance(g, dict) and "name" in g:
                            genre_name = str(g["name"]).lower()
                            if genre_name == genre.lower():
                                has_genre = True
                                break
                        j += 1

                # If this movie has the target genre, add it to result
                if has_genre:
                    result.append(movie)

                index += 1

        # 3. Traverse right subtree
        self._inorder_traversal(node.right, genre, start_year, end_year, result)



    def display(self, movies_array):
        index = 0
        total = movies_array.size()
        if total == 0:
            print("No movies found matching your criteria.")
            return
        while index < total:
            movie = movies_array.get(index)
            title = movie.get('title', 'N/A')
            release_date = movie.get('release_date', 'N/A')
            print(f"Index: {index}, Title: {title}, Year: {release_date}")
            index += 1