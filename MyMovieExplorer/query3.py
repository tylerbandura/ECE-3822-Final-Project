import os
import sys
from DataStructures.bst import BST
import pandas as pd

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

class Movie:
    def __init__(self, title, genre, year, movies):
        self.title = title
        self.genre = genre
        self.year = year
        self.movies = []
        self.left = None
        self.right = None

class FindMoviesByGenre:
    def __init__ (self):
        self.root = None





    def insert_movie(self, movie, year):
        if self.root is None:
            self.root = Movie(year, movie)
            return self.root
        else:
            self._insert_movie(movie, year, self.root)
    def _insert_movie(self, movie, node, year):
        if year < node.year:
            if movie.left:
                self._insert_movie(year, node.left, movie)
            else:
                movie.left = Movie(year, movie)
        elif year > node.year:
            if node.right:
                self._insert_movie(year, movie, node.right)
            else:
                node.right = Movie(year, movie)
        else:
            node.movies.append(movie)
    
    def search_by_genre(self, node, genre, start_years, end_years, movie_results=None):

        if movie_results is None:
            movie_results = []

        if self.root is None:
            return movie_results
        
        if start_years <= node.year <= end_years:
            for movie in node.movies:
                if movie["genre"].lower():
                    movie_results.append(movie)
        elif start_years < node.year:
            return self.search_by_genre(node.left, genre, start_years, end_years, movie_results)
        elif node.year < end_years:
            return self.search_by_genre(node.right, genre, start_years, end_years, movie_results)
        

    def load_movies(self, file_path="data/prototype_data/movies_metadata_small.csv"):
        try:
            df = pd.read_csv(file_path)
            MovieTree = BST()

            for _, row in df.iterrows():
                movie = {"title": row["title"], "genre": row["genre"], "year": int(row["year"]) }
                MovieTree._insert(movie["year"], movie)
        except FileNotFoundError:
            raise FileNotFoundError(f"ERROR: File not found")
        

    def main():
        genre = "Comedy"
        start_year = 1994
        end_year = 1996
        
        


        
        





 
 



