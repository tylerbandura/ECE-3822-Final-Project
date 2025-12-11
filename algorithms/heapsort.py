'''
file: DataStructures/heap.py

ZhaoXiang Lan, 12/4/2025

description:
using the basic heap structure to build both min-heap and max-heap.

Heap data structure description:
compare_func(a, b):
    return True if a should be above b
    return False otherwise
Example:
    min-heap: h = Heap(lambda a, b: a < b)
    max-heap: h = Heap(lambda a, b: a > b)
    or define a function separately and pass it in.
----------------------------------------------------------------------
'''
# input the root path
import os
import sys

# add the project root to sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# import Heap
from DataStructures.heap import Heap

# import array
from DataStructures.array import array

# min-heap class
class MinHeap:
    # constructor
    def __init__(self):
        # initialize a min-heap using the Heap class with tuple comparison
        # compare only the first element of tuples (the numeric value)
        self.heap = Heap(lambda a, b: a[0] < b[0] if isinstance(a, tuple) and isinstance(b, tuple) else a < b)

    # insert an new element
    def push (self, value):
        self.heap.push(value)

    # remove and return the minimum element
    def pop(self):
        return self.heap.pop()
    
    # return the minimum element without removing it
    def peek(self):
        return self.heap.peek()
    
    # return the size of the min-heap
    def size(self):
        return self.heap.size()
    
    # return whether the min-heap is empty
    def is_empty(self):
        return self.size() == 0
    
    # return all value
    def get_all_elements(self):
        # pop all elements and return them in an array
        elements = array()
        while not self.is_empty():
            element = self.pop()
            if element is not None:  # filter out None values
                elements.append(element)
        # return the array of elements
        return elements