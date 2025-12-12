"""
Docstring for tests.test2

test2.py

purpose: individual test for q2 (Find movie by actor)
"""
import os
import pickle
from MyMovieExplorer.query2 import FindByActor

from MyMovieExplorer.query2 import FindByActor

def test_query2():
    print("Testing Query 2: Find Movies by Actor...")
    
    DATA_DIR = "data"
    MOVIE_PATH = os.path.join(DATA_DIR, "id_to_movieData.pkl")
    RATING_PATH = os.path.join(DATA_DIR, "id_to_rating.pkl")
    ACTOR_PATH = os.path.join(DATA_DIR, "actorTable.pkl")

    # Load pickled objects
    with open(MOVIE_PATH, "rb") as f:
        id_to_movieData = pickle.load(f)
    with open(RATING_PATH, "rb") as f:
        id_to_rating = pickle.load(f)
    with open(ACTOR_PATH, "rb") as f:
        actorTable = pickle.load(f)

    q2 = FindByActor(actorTable, id_to_movieData, id_to_rating)

    # Test Case 1: Known Actor
    actor_name = "Tom hanks"
    result_array = q2.find_movies(actor_name)

    if result_array:
        print(f"\nMovies featuring {actor_name}:")
        # manually iterate
        index = 0
        while index < len(result_array):
            movie = result_array[index]
            print(f"- {movie['title']} (Rating: {movie['rating']:.2f})")
            index += 1
    else:
        print(f"No movies found for {actor_name}.")

    # Test Case 2: Unknown Actor
    actor_name = "Tom Hnaks"
    result_array = q2.find_movies(actor_name)

    if result_array:
        print(f"\nMovies featuring {actor_name}:")
        # manually iterate
        index = 0
        while index < len(result_array):
            movie = result_array[index]
            print(f"- {movie['title']} (Rating: {movie['rating']:.2f})")
            index += 1
    else:
        print(f"No movies found for {actor_name}.")




if __name__ == "__main__":
    try:
        test_query2()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: One of the files not found.")
    except IndexError:
        raise IndexError("Error: CSV missing 'actor_name' or 'movie_id' columns.")
