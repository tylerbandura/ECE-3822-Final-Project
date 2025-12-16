# add the project root to sys.path
import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)
    
from DataStructures.array import array
from algorithms.mergesort import merge_sort

def print_array(arr):
    i = 0
    while i < arr.size():
        print(arr.get(i), end=" ")
        i += 1
    print()

def main():
    a = array()
    a.append(5)
    a.append(2)
    a.append(9)
    a.append(1)
    a.append(6)
    a.append(3)

    print("Before sort:")
    print_array(a)

    sorted_a = merge_sort(a)

    print("After sort:")
    print_array(sorted_a)

if __name__ == "__main__":
    main()
