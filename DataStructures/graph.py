"""
file path: ECE-3822-Final-Project/DataStructures/graph.py

description:

date created: december 6th, 2025

author: Tony Mejia-Cuba
"""

class Graph:
    
    # constructor
    def __init__(self):
        # adjacency list node that will list nieghbors
        self.adj = {}
        # to be able to output actor a and b and thier movies
        self.edge_label = {}

    # function to add a node
    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    # function to add an edge
    def add_edge(self, src, dst, label=None):
        '''
       src : source node
       dst : destination node
       label : label for the edge aka movie name

       if the nodes do not exist or in this case the actors name not
       in the adjacency list we add them first. the ators are both 
       src and dst respectively.

       if actor a is in movie with b then we add b to a's 
       and vide versa. then we just store the movie in each edge
        '''
        self.add_node(src)
        self.add_node(dst)

        if dst not in self.adj[src]:
            self.adj[src].append(dst)

        if src not in self.adj[dst]:
            self.adj[dst].append(src)

        if label is not None:
            self.edge_label[(src, dst)] = label
            self.edge_label[(dst, src)] = label

    # function to get neighbors
    def get_neighbors(self, node):
        # if the node is in the adjacency list return its neighbors
        if node in self.adj:
            return self.adj[node]
        return []
    
    # function to check if a node exists
    def has_node(self, node):
        return node in self.adj
    
# end of Graph class

# end of file