'''
file: DataStructures/array.py
A simple implementation of a dynamic array data structure.
ZhaoXiang Lan, 12/4/2025

description:
This program defines a dynamic array class and a BucketArray class
----------------------------------------------------------------------
dynamic arrat(similar to Python list)
functions:
1. append(value): Append an element to the end of the array.
2. get(index): Get the element at the specified index.
3. set(index, value): Set the element at the specified index.
4. size(): Return the current size of the array.
5. display(): Return a string representation of the array.

example usage:
from array import array
arr = array()
arr.append(10)
arr.append(20)
print(arr.display())  # Output: [10, 20]  
value = arr.get(1)
print(value)         # Output: 20
arr.set(0, 15)
print(arr.display())  # Output: [15, 20]
----------------------------------------------------------------------
BucketArray (array of arrays)
functions:
1. set_bucket(index, value): Set the array at the specified bucket index.
2. get_bucket(index): Get the array at the specified bucket index.
3. add_to_bucket(bucket_index, value): Add an element to the array at the specified bucket index.
4. size(): Return the current size of the bucket array.
5. display(): Return a string representation of the bucket array.

example usage:
from array import BucketArray
bucket_arr = BucketArray()
add emelent to bucket 0
bucket_arr.add_to_bucket(0, 10)
bucket_arr.add_to_bucket(0, 20)
set bucket 1 directly
arr = array()
arr.append(30)
bucket_arr.set_bucket(1, arr)
print(bucket_arr.display())
Output:
0: [10, 20]
1: [30]
----------------------------------------------------------------------
'''

# dynamic array class
# 
class array:
    # constructor
    def __init__(self, capacity=5):
        # initialize the array with a given capacity
        # protected attributes
        self._capacity = capacity
        self._size = 0
        self._array = [None] * self._capacity

    # append an element to the end of the array
    def append(self, value):
        # check if resizing is needed
        if self._size == self._capacity:
            # double the capacity
            new_capacity = self._capacity * 2
            # create a new array and copy elements
            new_array = [None] * new_capacity
            # copy existing elements
            i = 0
            while i < self._size:
                new_array[i] = self._array[i]
                i += 1
            # update the new array and capacity
            self._array = new_array
            self._capacity = new_capacity

        # add the new element at the end
        self._array[self._size] = value
        self._size += 1

    # get method
    def get(self, index):
        # index bounds check
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        # get the element at the specified index
        return self._array[index]
    
    # set method
    def set(self, index, value):
        # index bounds check
        if index < 0:
            raise IndexError("Index cannot be negative")
        # expand the array if index exceeds current size
        while index >= self._size:
            self.append(None)
            self._size += 1
        # set the element at the specified index
        self._array[index] = value

    # size method
    def size(self):
        # return the current size of the array
        return self._size
    
    # display method
    def display(self):
        # create a string representation of the array
        result = "["
        # display the elements in the array
        for i in range(self._size):
            # convert the element to string
            value = str(self._array[i])
            # add the element to the result string
            result += value
            # add a comma if not the last element
            if i != self._size - 1:
                result += ", "
        # add the closing bracket
        result += "]"
        # return the result
        return (result)
    

# BucketArray class for containing arrays of arrays
class BucketArray:
    # constructor
    def __init__(self, bucket_capacity=5):
        # initialize the bucket array with a given capacity
        # protected attributes
        self._bucket = array(bucket_capacity)
        self._size = 0
        # fill the bucket with None values
        #
        while self._size < bucket_capacity:
            self._bucket.append(None)
            self._size += 1
    
    # set_bucket method
    def set_bucket(self, index, value):

        # index bounds check
        if index < 0:
            raise IndexError("Index cannot be negative")
        
        # expend the bucket if index exceeds current size
        while index >= self._size:
            self._bucket.append(None)
            self._size += 1

        # set the value at the specified index in the bucket array
        self._bucket.set(index, value)

    # get_bucket method
    def get_bucket(self, index):
        # index bounds check
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        # get the value at the specified index in the bucket array
        return self._bucket.get(index)
    
    # size method
    def size(self):
        # return the current size of the bucket array
        return self._size
    
    # add the element to the son array at the specified bucket index
    def add_to_bucket(self, bucket_index, value):
        # check the index bounds
        if bucket_index < 0:
            raise IndexError("Index cannot be negative")
        
        # expand the bucket if index exceeds current size
        while bucket_index >= self._size:
            self._bucket.append(None)
            self._size += 1

        # get the son array at the specified bucket index
        bucket = self._bucket.get(bucket_index)

        # if the son array does not exist, create a new one
        if bucket is None:
            bucket = array()
            self._bucket.set(bucket_index, bucket)

        # append the value to the son array
        bucket.append(value)

    # display method
    def display(self):
        # create a string representation of the bucket array
        result = ""

        # display each bucket
        i = 0

        while i < self._size:
            # get the son array at the specified bucket index
            bucket = self._bucket.get(i)
            # create the line for the current bucket
            # check if the bucket is None
            if bucket is None:
                # create the empty array when bucket is None
                line = str(i) + ": [None]"
            else:
                # display the son array
                line = str(i) + ": " + bucket.display()
            # swith to the next line if not the last bucket
            if i != self._size - 1:
                line += "\n"
            # add the line to the result
            result += line
            # increment the index to move to the next bucket
            i += 1
            
        # return the result
        return result