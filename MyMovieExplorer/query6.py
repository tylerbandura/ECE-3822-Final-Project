'''
file path: ECE-3822-Final-Project/MyMovieExplorer/query6.py

description: this is the code for query 6: find the shortest path between two actors.
             we will use the bfs algorithm to achieve this

author: Tony Mejia
'''

# import things
import sys
import os
import pickle
import pandas as pd

# Add project root to sys.path so Python can find DataStructures
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from DataStructures.BFS import BFS

# fuction to format actor names
def format_actor_name(name):
    return "".join(part.capitalize() for part in name.split())

# main fuction
def main():
    if len(sys.argv) == 3:
        actor1 = sys.argv[1].strip()
        actor2 = sys.argv[2].strip()
    elif len(sys.argv) == 1:
        # interactive mode
        print("enter two actor names to find the shortest path between them.")
        actor1 = input("Actor 1: ").strip()
        actor2 = input("Actor 2: ").strip()
    else:
        print("Usage: python query6.py [actor1 actor2]")
        sys.exit(1)

    actor1_key = actor1.lower()
    actor2_key = actor2.lower()

    # path to pickled_things folder
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
    PICKLE_DIR = os.path.join(PROJECT_ROOT, "pickled_things")

    try:
        with open(os.path.join(PICKLE_DIR, "pickled_graph.pkl"), "rb") as f:
            graph = pickle.load(f)
        with open(os.path.join(PICKLE_DIR, "pickled_movies.pkl"), "rb") as f:
            id_to_title = pickle.load(f)
    except Exception as e:
        print("ERROR: could not load pickled files:", e)
        sys.exit(1)

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
