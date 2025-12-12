'''
file: DataStructures/bst.py
Desctiption: This program is a simple implementation of our particular binary seach tree in Python.
    - This particular tree uses arrays to store movie information
Intructions to run:  type "python bst.py" in the terminal
Author: Tyler Bandura
Date: 12/8/2025
Email: tuu03215@temple.edu

'''

from DataStructures.array import array




'''Node class that represents each node in the tree. A node can have at max 2 children.'''
# The left child must be less than the parent, and the right node must be greater than the parent.
class Node:
    def __init__(self, year): # constructor
        # Initialization. At the start, a node has a value but no children.
        self.left = None
        self.right = None
        self.parent = None
        self.node_movies = array() # initialize array to store movies
        self.node_year = year

        
''' The main BinarySearchTree (BST) class.'''       
class BST:
    def __init__(self): # contructor that initializes tree
        self.root = None # upon initialization, a tree does not have a root

        

    ''' Function for adding a year into the binary search tree, with the year serving as a value (if this were a traditional BST).'''  
    def insert(self, year, movie):
        if self.root is None:
            # Give the root a value
            self.root = Node(year)
            self.root.node_movies.append(movie)
        else:
            # Inserts the root into the tree
            self._insert(year, movie, self.root)

    def _insert(self, year, movie, node):
        if year < node.node_year:
            # If the parent node already has a left child, insert to the left of it
            if node.left:
                self._insert(year, movie, node.left)
                node.left.parent = node
            else:
                # the inserted node is now the left child of the parent
                node.left = Node(year)
                node.left.node_movies.append(movie)
                node.left.parent = node

        elif year > node.node_year:
            if node.right:
                # If the parent node already has a right child, insert to the right of it
                self._insert(year, movie, node.right)
                node.right.parent = node
            else:
                # the inserted node is now the right child of the parent
                node.right = Node(year)
                node.right.node_movies.append(movie)
                node.right.parent = node

        else:
            # If the year is already in the tree, just append the movie to that year's movie list
            node.node_movies.append(movie)

    '''Function to search for movies by the range of years'''
    def get_movies_by_year_range(self, node, start_year, end_year, movies_list):
        if node is None:
            return # Returns nothing if node is None
        # Search left subtree if the year if the current movie is greater than the start year
        if node.node_year > start_year:
            self.get_movies_by_year_range(node.left, start_year, end_year, movies_list)
        
        # If a movie is the range, add to the list of movies
        if start_year <= node.node_year <= end_year:
            i = 0
            while i < len(node.node_movies):
                movie = node.node_movies[i]
                movies_list.append(movie)
                i += 1
        # Search right subtree
        if node.node_year < end_year:
            self.get_movies_by_year_range(node.right, start_year, end_year, movies_list)
    '''Function that handles all movies in the given range'''
    def movie_in_range(self, start_year, end_year):
        movies_list = array()
        self.get_movies_by_year_range(self.root, start_year, end_year, movies_list)
        return movies_list
    