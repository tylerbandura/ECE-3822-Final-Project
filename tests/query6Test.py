"""
file: /home/tul34363/ece_3822LABWORK/ECE-3822-Final-Project/tests/query6Test.py

description:
    Test code for query6 shortest actor path logic.
    Uses a small hand-built graph instead of pickled data.

author:
    Tony Mejia
"""

# imports
import sys
import os

# add project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from DataStructures.graph import Graph
from DataStructures.BFS import BFS

# fuction to build test graph
def build_test_graph():
    """
    Creates a small actor graph:

        Tom Hanks -- Forrest Gump -- Robin Wright -- Wonder Woman -- Gal Gadot
    """

    g = Graph()

    # add edges
    g.add_edge("Tom Hanks", "Robin Wright", "Forrest Gump")
    g.add_edge("Robin Wright", "Gal Gadot", "Wonder Woman")

    return g

# function to test shortest path
def test_shortest_path():
    '''
    this fucion will test the shortest path from Tom Hanks to Gal Gadot
    using the our graph

    we call the bfs shortest path function and print the result

    then we assert the result to make sure it is correct
    '''
    graph = build_test_graph()
    bfs = BFS(graph)

    start = "Tom Hanks"
    end = "Gal Gadot"

    path = bfs.shortest_path(start, end)

    print("Expected path:")
    print("Tom Hanks -> Robin Wright -> Gal Gadot\n")

    print("Actual path:")
    print(path)

    # assert to debug and test correctness
    assert path == [
        "Tom Hanks",
        "Robin Wright",
        "Gal Gadot"
    ], "Shortest path is incorrect"

# run main test
if __name__ == "__main__":
    print("Running Query 6 tests...\n")
    test_shortest_path()
    print("\nAll tests passed.")

# end of file