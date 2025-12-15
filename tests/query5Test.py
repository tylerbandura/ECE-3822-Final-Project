"""
file: ECE-3822-Final-Project/tests/query5Test.py

description:
    Test code for query5 movie suggestion logic.
    Uses a small hand-built movie database.

author:
    Tony Mejia-Cuba
"""

# imports
import sys
import os

# add project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from MyMovieExplorer.query5 import Movie, MovieDatabase

# fuction to build test movie database
def build_test_database():
    db = MovieDatabase()

    # create test movies
    m1 = Movie(1, "Inception", ["Sci-Fi"], 8.8)
    m2 = Movie(2, "Interstellar", ["Sci-Fi"], 8.6)
    m3 = Movie(3, "The Matrix", ["Sci-Fi"], 8.7)
    m4 = Movie(4, "Titanic", ["Romance"], 7.8)

    # add movies to database
    db.add_movie(m1)
    db.add_movie(m2)
    db.add_movie(m3)
    db.add_movie(m4)

    return db

# function to test movie suggestions
def test_suggest_movies():
    '''
    this fucion will test the suggest movies function
    using our small movie database

    we call the suggest movies function and print the result
    then we assert the result to make sure it is correct
    '''
    db = build_test_database()

    suggestions = db.suggest_movies("Inception", top_k=3)

    print("Suggestions for 'Inception':")
    print(suggestions)

    # inception should NOT recommend itself
    assert "Inception" not in suggestions, "Input movie was included in suggestions"

    # movies of same genre should appear
    assert "Interstellar" in suggestions, "Expected Interstellar in suggestions"
    assert "The Matrix" in suggestions, "Expected The Matrix in suggestions"

    # romance movie should not appear
    assert "Titanic" not in suggestions, "Romance movie incorrectly suggested"

# run main test
if __name__ == "__main__":
    print("Running Query 5 tests...\n")
    test_suggest_movies()
    print("\nAll tests passed.")

# end of file