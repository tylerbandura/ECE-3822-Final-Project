'''
file: DataStructures/bst.py
Desctiption: This program is a simple implementation of a binary seach tree in Python.
Intructions to run:  type "python bst.py" in the terminal
Author: Tyler Bandura
Date: 12/8/2025
Email: tuu03215@temple.edu

functions include:
    - search(): checks if a specific value is in the tree.
    - insert(): Inserts a node into the tree.
    - find_min(): Returns the smallest value of the tree:
    - find_max(): Returns the largest value in the tree.
    - delete(): Deletes a value from the tree.
        If the deleted node has 2 children, the in-order successor (The max node in the left subtree OR the min node in the right subtree) takes it's place.
    - inorder_traverse(): Performs an in-order traversal of the tree.
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
        self.node_movies = array()
        self.node_year = year

        
''' The main BinarySearchTree (BST) class.'''       
class BST:
    def __init__(self): # contructor that initializes tree
        self.root = None # upon initialization, a tree does not have a root

        

    ''' Function for adding a value into the binary search tree.'''  
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
                # If the parent node already has a rightt child, insert to the right of it
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

    
    def get_movies_by_year_range(self,node, start_year, end_year, movies_list):
        if node is None:
            return
        
        if node.node_year > start_year:
            self.get_movies_by_year_range(node.left, start_year, end_year, movies_list)
        
        if start_year <= node.node_year <= end_year:
            i = 0
            while i < len(node.node_movies):
                movie = node.node_movies[i]
                movies_list.append(movie)
                i += 1
        
        if node.node_year < end_year:
            self.get_movies_by_year_range(node.right, start_year, end_year, movies_list)

    def movie_in_range(self, start_year, end_year):
        movies_list = array()
        self.get_movies_by_year_range(self.root, start_year, end_year, movies_list)
        return movies_list
    