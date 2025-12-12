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
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    # Divide the array into two halves: left_half and right_half
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursive calls to merge_sort for sorting the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted left and right halves
    return merge(left_half, right_half)
    
def merge(left, right):
    result = array()  # List to store the merged result
    i = j = 0  # Pointers for iterating through the left and right halves
    
    # Compare elements from the left and right halves and add them to the result list in the correct order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add any remaining elements from the left half to the result list
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Add any remaining elements from the right half to the result list
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result