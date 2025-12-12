'''
file path: ECE-3822-Final-Project/MyMovieExplorer/query5.py

descripton: this code will pickel the hash table for me
            ot use in query 5 to suggest movies
'''

import os
import sys
import pickle
import pandas as pd

# Add the parent directory to Python's path so we can import MyMovieExplorer
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

# macros to find the csv file:
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) 
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR) 
MOVIES_CSV = os.path.join(PROJECT_ROOT, "data", "prototype_data", "movies_metadata_small.csv")
RATINGS_CSV = os.path.join(PROJECT_ROOT, "data", "prototype_data", "ratings_small.csv")

from MyMovieExplorer.query5 import Movie, MovieDatabase

# path to pickled folder
PICKLE_DIR = os.path.join(PROJECT_ROOT, "pickled_things")
os.makedirs(PICKLE_DIR, exist_ok=True)


def parse_genres(genres_raw):
    """
    Convert genre string from CSV into a list of genre names.
    Example input:
    "[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}]"
    returns: ["Animation", "Comedy"]
    """
    if genres_raw == "unknown" or genres_raw.strip() == "":
        return []

    try:
        parsed = ast.literal_eval(genres_raw)  # convert string → python list
        names = [g["name"] for g in parsed if "name" in g]
        return names
    except:
        return []

# main function to build and pickle movie database
def main():
    # create database
    db = MovieDatabase()

    try:
        # read movies in csv
        movies_df = pd.read_csv(MOVIES_CSV, dtype=str)

        # get the data from the columns by thier names and clean it, we do this because
        # some entries are missing data
        movies_df['title'] = movies_df['title'].fillna("unknown title")
        movies_df['genres'] = movies_df['genres'].fillna("unknown")
        movies_df = movies_df.dropna(subset=['id']) # drop rows with missing ids because we wont be able to use them
        movies_df['id'] = movies_df['id'].astype(int) # convert ids to integers
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)

    # repeat the same logic as above for the ratings csv
    try:
        ratings_df = pd.read_csv(RATINGS_CSV, dtype=str)
        ratings_df['movieId'] = pd.to_numeric(ratings_df['movieId'], errors='coerce')
        ratings_df['rating'] = pd.to_numeric(ratings_df['rating'], errors='coerce')
        ratings_df = ratings_df.dropna(subset=['movieId'])
        ratings_df['movieId'] = ratings_df['movieId'].astype(int)
    except Exception as e:
        print(f"Error reading Ratings CSV file: {e}")
        sys.exit(1)

    # find the average rating for each movieid so that we use them in our movie objects
    # the code below means group by movieId and then take the mean of the ratings for each group
    avg_ratings = ratings_df.groupby('movieId')['rating'].mean().reset_index()
    avg_ratings.rename(columns={'movieId':'id'}, inplace=True) # rename for merging since we are using two csv files

    # merge average ratings into movies_df
    merged = pd.merge(movies_df, avg_ratings, on='id', how='left')

    # fill missing ratings with 0
    merged['rating'] = merged['rating'].fillna(0.0)

    # build movie objects
    for _, row in merged.iterrows():
        movie = Movie(
            movie_id=row['id'],
            title=row['title'],
            genre=row['genres'],
            rating=float(row['rating']        )
        )
        db.add_movie(movie)
    
    # time to pickle
    # we pickle by writing to a file using pickle.dump
    pickle_path = os.path.join(PICKLE_DIR, "pickled_movie_db.pkl")
    # with a new open file in write binary
    with open(pickle_path, 'wb') as f:
        # we weirte the database object to the file and then save it to disk as pickled_movie_db.pkl
        pickle.dump(db, f)
    print(f"databased aaved as pickled_movie_db.pkl")

if __name__ == "__main__":
    main()

# enf of main

# end of file