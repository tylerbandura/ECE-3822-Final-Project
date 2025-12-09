"""
query2.py

Purpose: Find all movies by a given actor

This file will build two hashtables:
1. actor: actor_name(lower) -> [movie_id...]
2. id_to_title: movie_id -> title

To keep our load factor less than 0.75 (aiming for a = 0.65)
    actorTable: buckets = 60000/0.65 = 92000 (bucket size = 100000)
    id_to_title: buckets = 45000/0.65 = 69000 (bucketsize = 70000)

"""
import pandas as pd
from DataStructures.hashTable import HashTable
from DataStructures.array import array

class FindByActor:
    def __init__(self):
        # hashtable for actor
        self.actorTable = HashTable(size=100000)
        # hashtable for id
        self.id_to_title = HashTable(size=70000)

        self.load_movies()
        self.load_actors()

    def load_movies(self, file_path="data/prototype_data/movies_metadata_small.csv"):
        # loads movies IDs and titles from database into id_to_title hashtable, returns # of movies loaded

        try:
            df = pd.read_csv(file_path)
            rows = df.values.tolist()
            header = list(df.columns)

            id_index = header.index("id")
            title_index = header.index("title")

            for i, row in enumerate(rows):
                movie_id = str(row[id_index]).strip()
                title = str(row[title_index]).strip() if row[title_index] else "(Unknown Title)"
                if movie_id != "":
                    self.id_to_title.insert(movie_id, title)

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: {file_path} not found.")
        except KeyError:
            raise KeyError("Error: CSV missing 'id' or 'title' colums.")

    def load_actors(self, file_path="data/prototype_data/cleaned_actors_small.csv"):
        # loads actor and movie ids relationships, returns number of actors processed

        try:
            df = pd.read_csv(file_path)
            rows = df.values.tolist()
            header = list(df.columns)

            actor_index = header.index("actor_name")
            movie_index = header.index("movie_id")

            for i, row in enumerate(rows):
                actor = str(row[actor_index]).strip().lower() # make lowercase for consistent lookups
                movie_id = str(row[movie_index]).strip()

                #skip invalid rows
                if actor == "" or movie_id == "":
                    continue

                title = self.id_to_title.lookup(movie_id)
                if title is None:
                     title = "(Unknown Title)"

                    # Insert or update list of titles
                movie_array = self.actorTable.lookup(actor)
                if movie_array is None:
                    movie_array = array()
                    movie_array.append(title)
                    self.actorTable.insert(actor, movie_array)
                else:
                    movie_array.append(title)
                    self.actorTable.insert(actor, movie_array)

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: {file_path} not found.")
        except KeyError:
            raise KeyError("Error: CSV missing 'actor_name' or 'movie_id' columns.")

    def find_movies(self, actor_name):
        # returns the list of movie titles for a given actor, returns None if not found

        if not actor_name:
            return None
        actor_key = actor_name.strip().lower() # make lowercase for consistency
        return self.actorTable.lookup(actor_key)
