'''
file path: ECE-3822-Final-Project/MyMovieExplorer/query6.py

description: this is the code for query 6: find the shortest path between two actors.
             we will use the bfs algorithm to achieve this

author: Tony Mejia
'''

# import things
import sys
import os
import pandas as pd

from DataStructures.graph import Graph
from DataStructures.BFS import BFS

# easy access to csv files, HARD CODED CAUSE ITS BETTER THAN ASKING
# A USER FOR A DATASET

# Get the project root directory (one level up from MyMovieExplorer)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# Build paths relative to project root
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

def format_actor_name(name):
    return "".join(part.capitalize() for part in name.split())

def main():
    if len(sys.argv) != 3:
        print("Usage: python query6.py 'Actor Name 1' 'Actor Name 2'")
        sys.exit(1)
    
    actor1 = sys.argv[1].strip()
    actor2 = sys.argv[2].strip()

    actor1_key = actor1.lower()
    actor2_key = actor2.lower()

    print("\nFinding shortest path between '{}' and '{}'...\n".format(actor1, actor2))
    id_to_title = load_movies(MOVIES_CSV)

    print("Building actor graph, this might take a moment, thank you...")
    graph = build_actor_graph(ACTORS_CSV, id_to_title)

    lower_to_original = {name.lower(): name for name in graph.adj.keys()}

    if actor1_key not in lower_to_original:
        print("Actor '{}' not found in dataset.".format(actor1))
        sys.exit(1)
    if actor2_key not in lower_to_original:
        print("Actor '{}' not found in dataset.".format(actor2))
        sys.exit(1)
    
    start = lower_to_original[actor1_key]
    end = lower_to_original[actor2_key]

    bfs = BFS(graph)
    path = bfs.shortest_path(start, end)

    if path is None:
        print("No connection found between '{}' and '{}'.".format(actor1, actor2))
        sys.exit(0)

    print("Shortest path found between '{}' and '{}':\n".format(actor1, actor2))

    for i in range(len(path)):
        print(format_actor_name(path[i]))
        if i + 1 < len(path):
            movie = graph.get_edge_data(path[i], path[i + 1]) or "(Unknown Movie)"
            print("  └── through ", movie)

if __name__ == "__main__":
    main()

# end of file
