"""
Docstring for data.build_data

build_data.py

purpose: Build and pickle all database csv for queries. This will ensure that we are
            not waiting a long time to load out database

how it works: Builds all four database files, builds core hash tables, pickles them to /data/

note: Query 5 and 6 use a separate pickled database built by tony and those are not affected by 
        this file.
"""
import os
import pickle
import pandas as pd
from DataStructures.hashTable import HashTable

def build_all_data():
    data_dir = "data/prototype_data" # folder where all databases are
    out_dir = "data" # where the .pkl files will be saved

    os.makedirs(out_dir, exist_ok=True)

    print("Building and Pickling data...")

    # getting full metadata from movie id
    # used by queries 1-4
    # wanted load factor: ~0.7
    # 45,000/0.70 = 64,300 -> 70,000 (45,000 is the number of lines in the original database file)
    id_to_movieData = HashTable(size=70000)

    movies_path = os.path.join(data_dir, "movies_metadata_small.csv")
    movies_df = pd.read_csv(movies_path, low_memory=False)
    movies_df = movies_df.dropna(subset=["id"])

    for _, row in movies_df.iterrows():
        movie_id = str(row["id"]).strip()
        if not movie_id:
            continue

        movie_data = {
            "title": str(row.get("title", "(Unknown Title)")),
            "original_title": str(row.get("original_title", "")),
            "genres": str(row.get("genres", "")),
            "release_date": str(row.get("release_date", "")),
            "runtime": float(row.get("runtime", 0)) if not pd.isna(row.get("runtime")) else 0.0,
            "budget": float(row.get("budget", 0)) if not pd.isna(row.get("budget")) else 0.0,
            "revenue": float(row.get("revenue", 0)) if not pd.isna(row.get("revenue")) else 0.0,
            "overview": str(row.get("overview", "")),
        }

        id_to_movieData.insert(movie_id, movie_data)

    print(f"Loaded {len(movies_df)} movies into id_to_movieData")

    # ratings
    # used by query 1,2,4
    # 45,000 lines, so same as before our hashtable size should be 70000

    id_to_rating = HashTable(size=70000)

    ratings_path = os.path.join(data_dir, "ratings_small.csv")
    ratings_df = pd.read_csv(ratings_path)
    ratings_df["movieId"] = pd.to_numeric(ratings_df["movieId"], errors="coerce")
    ratings_df["rating"] = pd.to_numeric(ratings_df["rating"], errors="coerce")
    ratings_df = ratings_df.dropna(subset=["movieId"])

    avg_ratings = ratings_df.groupby("movieId")["rating"].mean().reset_index()

    for _, row in avg_ratings.iterrows():
        movie_id = str(int(row["movieId"]))
        avg_rating = float(row["rating"])
        id_to_rating.insert(movie_id, avg_rating)

    print(f"Loaded ratings for {len(avg_ratings)} movies into id_to_rating")

    # cleaned_actors.csv
    # used by query 2

    actorTable = HashTable(size=360000)

    actors_path = os.path.join(data_dir, "cleaned_actors_small.csv")
    actors_df = pd.read_csv(actors_path)

    for _, row in actors_df.iterrows():
        actor_name = str(row["actor_name"]).strip().lower()
        actor_id = str(row.get("actor_id", "")).strip()
        character_name = str(row.get("character_name", "")).strip()
        movie_id = str(row["movie_id"]).strip()

        if not actor_name or not movie_id:
            continue

        # Lookup existing list or create new one
        movie_list = actorTable.lookup(actor_name)
        if movie_list is None:
            movie_list = []

        # Append dictionary entry for this movie appearance
        movie_entry = {
            "movie_id": movie_id,
            "actor_id": actor_id,
            "character_name": character_name,
        }
        movie_list.append(movie_entry)

        # Reinsert into hash table
        actorTable.insert(actor_name, movie_list)

    print(f"Loaded {len(actors_df)} actor entries into actorTable")

    # save all pickled tables

    with open(os.path.join(out_dir, "id_to_movieData.pkl"), "wb") as f:
        pickle.dump(id_to_movieData, f)

    with open(os.path.join(out_dir, "id_to_rating.pkl"), "wb") as f:
        pickle.dump(id_to_rating, f)

    with open(os.path.join(out_dir, "actorTable.pkl"), "wb") as f:
        pickle.dump(actorTable, f)

    print("\nAll pickled hash tables successfully saved under /data/!\n")


if __name__ == "__main__":
    build_all_data()

