"""
Docstring for tests.test2

test2.py

purpose: individual test for q2 (Find movie by actor)
"""
import os, sys

from MyMovieExplorer.query2 import FindByActor

def test_query2():
    print("Testing Query 2: Find Movies by Actor...")

    q2 = FindByActor()

    # Test Case 1: Known Actor
    actor_name = "Tom hanks"
    result_array = q2.find_movies(actor_name)

    if result_array is not None:
        print(f"\nMovies featuring {actor_name}:")
        for i in range(result_array.size()):
            print("-", result_array.get(i))
    else:
        print(f"No movies found for {actor_name}.")

    # Test Case 2: Unknown Actor
    actor_name = "Tom Hnaks"
    result_array = q2.find_movies(actor_name)

    if not result_array:
        print(f"\nCorrectly handled missing actor: {actor_name}")
    else:
        print(f"\nUnexpected results for {actor_name}: {result_array}")



if __name__ == "__main__":
    try:
        test_query2()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: One of the files not found.")
    except IndexError:
        raise IndexError("Error: CSV missing 'actor_name' or 'movie_id' columns.")
