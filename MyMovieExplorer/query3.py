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

import DataStructures.array as array




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

    '''Function for finding if a certain value is in the tree. Returns True if so.'''
    '''
    value = target value that we are looking for in the tree.
    '''
    '''
    def search(self, value):
        # sets current node to be the start (root)
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None:
            return False
        if node.node_year == value:
            return True
        elif value < node.node_year:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)
    '''
    
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
    

    '''Function to perform an in-order traversal of the tree.'''
    def inorder_traverse(self):
        # Begin traversal from the root node
        self._inorder_traverse(self.root)
    def _inorder_traverse(self, node):
        if node is not None:
            # Traverses left subtree
            self._inorder_traverse(node.left)
            # Prints node values in order (smallest to largest)
            print(node.value)
            # Traverses right subtree
            self._inorder_traverse(node.right)


    '''Function to find minimum value of the tree'''
    def find_min(self):
        if self.root is None:
            # cannot find minimum of empty tree
            raise ValueError("Empty.")
        # Set current node to root
        curr = self.root
        # Go down left subtree until the end is reached; the end node is the minimum value
        while curr.left is not None:
            curr = curr.left
            # Return value of minimum node
        return curr.value
    

    '''Function to find maximum value of tree'''
    def find_max(self):
        if self.root is None:
            # cannot find maximum of empty tree
            raise ValueError("Empty.")
        # Set current node to root
        curr = self.root
        # Go down rightt subtree until the end is reached; the end node is the maximum value
        while curr.right is not None:
            curr = curr.right
        # Return value of maximum node
        return curr.value
    

    '''Function to delete node from the tree.'''

    '''
    There are 3 cases for the delete function:
        - Case 1: The node to be deleted has no children (leaf), can simply be removed
        - Case 2: The node has 1 child, in which case that child will move into the spot of the deleted node
        - Case 3: The node has 2 children, in which case the in-order successor (The minimum of the right subtree) will replace the deleted node.
    
    '''
    def delete(self, value=None, node=None):
        if node is None:
            raise ValueError("Node not in tree.")
        # Begin at root
        node = self.root
        # Traverse left tree
        if value < node.value:
            node.left = self.delete(node.left, value)
            # Traverse right tree
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else: # The node we want to delete has been founf
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # In-order successor is min value of right subtree
            successor = self.find_min(node.right)
            # assign deleted node's value to the successor
            node.value = successor.value
            # Delete the successor
            node.right = self.delete(node.right, successor.value)

        return node
        
        

        
            
'''
test case for each BST function
if __name__ == "__main__":
    bst = BST() # make a new bst object
    bst.insert(5)
    bst.insert(10)
    bst.insert(4)
    bst.insert(8)
    bst.insert(12)
    bst.insert(2)
    bst.inorder_traverse()
    print(bst.find_min())
    print(bst.find_max())
    print(bst.search(7))
    bst.delete(5)
    bst.inorder_traverse()

'''
    


    




            
