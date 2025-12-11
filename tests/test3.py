import os
import sys

from MyMovieExplorer.query3 import FindMoviesByGenre

def test3():
    print("Testing Query 3")

    q3 = FindMoviesByGenre()

    genre =input("Enter a genre to search")
    start_year =input("Enter a start year for search")
    end_year = input("Enter a end year for search")

    q3.load_movies()

    q3.search_by_genre(node=)




