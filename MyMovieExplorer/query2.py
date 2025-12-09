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
import csv
from DataStructures.hashTable import HashTable

class FindByActor:
    def __init__(self):
        # hashtable for actor
        self.actorTable = HashTable(size=100000)
        # hashtable for id
        self.id_to_title = HashTable(size=70000)

    def load_movies(self):
        try:
            with open("data/prototype_data/movies_metadata_small.csv", newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    movie_id = row["id"].strip()
                    title = row["title"].strip() if row["title"] else "(Unknown Title)"
                    self.id_to_title.insert(movie_id, title)
        except FileNotFoundError:
            print("Error: data/movies_metadata_small.csv not found.")
        except KeyError:
            print("Error: CSV missing 'id' or 'title' columns.")

    def load_actors(self):
        try:
            with open("data/prototype_data/cleaned_actors_small.csv", newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    actor = row["actor_name"].strip()
                    movie_id = row["movie_id"].strip()
                    title = self.id_to_title.lookup(movie_id)

                    # If title not found, use placeholder
                    if title is None:
                        title = "(Unknown Title)"

                    # Insert or update list of titles
                    movies = self.actorTable.lookup(actor)
                    if movies is None:
                        self.actorTable.insert(actor, [title])
                    else:
                        movies.append(title)
                        self.actorTable.insert(actor, movies)
        except FileNotFoundError:
            print("Error: data/cleaned_actors_small.csv not found.")
        except KeyError:
            print("Error: CSV missing 'actor_name' or 'movie_id' columns.")

    def find_movies(self, actor_name):
        if not actor_name:
            print("No actor name given.")
            return
        results = self.actorTable.lookup(actor_name.strip())
        if results is None:
            print("\nNo movies found for", actor_name)
        else:
            print("\nMovies featuring", actor_name + ":")
            for title in results:
                print("-", title)
