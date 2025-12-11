'''
file: DataStructures/heap.py

ZhaoXiang Lan, 12/4/2025

description:
The heap data structure implementation.


compare_func(a, b):
    return True if a should be above b
    return False otherwise

Example:
    min-heap: h = Heap(lambda a, b: a < b)
    max-heap: h = Heap(lambda a, b: a > b)
    or define a function separately and pass it in.

----------------------------------------------------------------------
'''

# import array
from DataStructures.array import array

# heap class
class Heap:
    # constructor
    def __init__(self, compare_function):
        self.data  = array()
        self.compare = compare_function

    # get the size of the heap
    def size(self):
        # return the number of elements in the heap
        return self.data.size()
    
    # return the root element of the heap
    def peek(self):
        # return None if heap is empty
        if self.size() == 0:
            return None
        # return the root element
        return self.data.get(0)
    
    # push an element into the heap
    def push(self, value):
        # add the element to the end of the array
        self.data.append(value)
        # heapify up from the last index
        self.heapify_up(self.size() - 1)

    # pop the root element from the heap
    def pop(self):
        # set the curren size of the heap n
        n = self.size()
        # return None if heap is empty
        if n == 0:
            return None
        
        # get the root element
        root = self.data.get(0)

        # get the last element
        last_element = self.data.get(n - 1)

        # remove the last element
        self.data.set(n-1, None)
        self.data._size -= 1

        if self.size() > 0:
            # move last element to root
            self.data.set(0, last_element)
            # heapify down from the root
            self.heapify_down(0)
        
        # return the root element
        return root

    # heapify up method
    def heapify_up(self, index):
        while index > 0:
            # get the parrent index
            parent_index = (index - 1) // 2
            # get the values
            child_value = self.data.get(index)
            # get the parent value
            parent_value = self.data.get(parent_index)

            # compare child and parent
            if self.compare(child_value, parent_value):
            # swap child and parent
                self.data.set(index, parent_value)
                self.data.set(parent_index, child_value)
                # move to parent index
                index = parent_index
            else:
                break

    # heapify down method
    def heapify_down(self, index):
        # get the current size of the heap
        n = self.size()

        while index < n:
            # get the left and right child indices
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            # assume the current index is the largest/smallest
            best_index = index

            # get the best value
            best_value = self.data.get(best_index)

            # compare with left child
            if left_index < n:
                # get the left child value
                left_value = self.data.get(left_index)
                # compare left child with best value
                if self.compare(left_value, best_value):
                    # update best index and value if left child is better
                    best_index = left_index
                    best_value = left_value

            # compare with right child
            if right_index < n:
                # get the right child value
                right_value = self.data.get(right_index)
                # compare right child with best value
                if self.compare(right_value, best_value):
                    # update best index and value if right child is better
                    best_index = right_index
                    best_value = right_value

            # check if the best index is different from the current index
            if best_index == index:
                # heap property is satisfied
                break
            else:
                # swap current index with best index
                current_value = self.data.get(index)
                self.data.set(index, best_value)
                self.data.set(best_index, current_value)
                # move to best index
                index = best_index