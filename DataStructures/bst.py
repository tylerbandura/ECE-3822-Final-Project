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






'''Node class that represents each node in the tree. A node can have at max 2 children.'''
# The left child must be less than the parent, and the right node must be greater than the parent.
class Node:
    def __init__(self, value): # constructor
        # Initialization. At the start, a node has a value but no children.
        self.left = None
        self.right = None
        self.value = value
''' The main BinarySearchTree (BST) class.'''       
class BST:
    def __init__(self): # contructor that initializes tree
        self.root = None # upon initialization, a tree does not have a root

        

    ''' Function for adding a value into the binary search tree.'''  
    def insert(self, value):
        if self.root is None:
            # Give the root a value
            self.root = Node(value)
        else:
            # Inserts the root into the tree
            self._insert(value, self.root)
    def _insert(self, value, node):
        if value < node.value:
            # If the parent node already has a left child, insert to the left of it
            if node.left:
                self._insert(value, node.left)
            else:
                # the inserted node is now the left child of the parent
                node.left = Node(value)
        else:
            if node.right:
                # If the parent node already has a rightt child, insert to the right of it
                self._insert(value, node.right)
            else:
                # the inserted node is now the right child of the parent
                node.right = Node(value)
    '''Function for finding if a certain value is in the tree. Returns True if so.'''
    '''
    value = target value that we are looking for in the tree.
    '''
    def search(self, value):
        # sets current node to be the start (root)
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)



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
            return None
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
    


    




            