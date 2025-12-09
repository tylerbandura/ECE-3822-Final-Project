'''
file path: ECE-3822-Final-Project/pickled_things/pickled_graph.py

description: this code is used to create a pickled graph object from the
            cleaned actor and movie datasets for faster loading times.

author: Tony Mejia

Note from author: i picked here because after leanring what pickling is,
i realized that loading the graph from csv every time would be inefficient.
so i made this code to run the csv here with the graph since the graph is the 
only things that loads the csv. knowiong that it was a clear choice to only pickle
the graph class.
'''

import os
import sys
import pandas as pd
import pickle

# Add project root to sys.path so Python can find DataStructures
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from DataStructures.graph import Graph

# Get the project root directory (current script)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

ACTORS_CSV = os.path.join(PROJECT_ROOT, "data", "prototype_data", "cleaned_actors_small.csv")
MOVIES_CSV = os.path.join(PROJECT_ROOT, "data", "prototype_data", "movies_metadata_small.csv")

# function to load movies from csv to code
def load_movies(movie_csv):
    try:
        df = pd.read_csv(movie_csv, dtype=str)
        df['title'] = df['title'].fillna("Unknown Title")
        id_to_title = pd.Series(df['title'].values, index=df['id'].str.strip()).to_dict()
    except Exception as e:
        print("ERROR: could not open csv file:", e)
        sys.exit(1)
    return id_to_title

def build_actor_graph(actor_csv, id_to_title):
    graph = Graph()
    try:
        df = pd.read_csv(actor_csv, dtype=str)
        df['actor_name'] = df['actor_name'].str.strip()
        df['movie_id'] = df['movie_id'].str.strip()

        # Group actors by movie
        movie_cast = df.groupby('movie_id')['actor_name'].apply(list).to_dict()

        for movie_id, cast in movie_cast.items():
            title = id_to_title.get(movie_id, "(Unknown Title)")
            for i in range(len(cast)):
                for j in range(i + 1, len(cast)):
                    actor1 = cast[i]
                    actor2 = cast[j]
                    graph.add_edge(actor1, actor2, title)
    except Exception as e:
        print("ERROR: could not open actor csv:", e)
        sys.exit(1)
    return graph

if __name__ == "__main__":
    print("Loading movie data...")
    id_to_title = load_movies(MOVIES_CSV)

    print("Building actor graph...")
    actor_graph = build_actor_graph(ACTORS_CSV, id_to_title)

    # build the path for the pickled graph
    with open("pickled_graph.pkl", "wb") as f:
        pickle.dump(actor_graph, f)

    with open("pickled_movies.pkl", "wb") as f:
        pickle.dump(id_to_title, f)

    print("built pickled graph and movie title dictionary successfully.")
