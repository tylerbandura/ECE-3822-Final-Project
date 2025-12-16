'''
file: algorithms/mergesort.py
ZhaoXiang Lan, 12/12/2025

description:
merge sort algorithm implementation
'''
# input the root path
import os
import sys

# add the project root to sys.path for running the module
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# inport necessary modules
from DataStructures.array import array


def merge_sort(arr):
    # Base case: if the length of the array is 1 or less, it is already sorted
    if arr.size() <= 1:
        return arr
    
    left = array()
    right = array()

    mid = arr.size() // 2
    i = 0
    while i < mid:
        left.append(arr.get(i))
        i += 1

    while i < arr.size():
        right.append(arr.get(i))
        i += 1

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
    
def merge(left, right):
    result = array()  # List to store the merged result
    i = j = 0  # Pointers for iterating through the left and right halves
    
    # Compare elements from the left and right halves and add them to the result list in the correct order
    while i < left.size() and j < right.size():
        if left.get(i) <= right.get(j):
            result.append(left.get(i))
            i += 1
        else:
            result.append(right.get(j))
            j += 1
    # Add any remaining elements from the left half to the result list
    while i < left.size():
        result.append(left.get(i))
        i += 1
    
    # Add any remaining elements from the right half to the result list
    while j < right.size():
        result.append(right.get(j))
        j += 1
    
    return result