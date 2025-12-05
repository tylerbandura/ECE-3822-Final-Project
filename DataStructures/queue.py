'''
file: DataStructures/queue.py
A simple implementation of a circular queue data structure.
ZhaoXiang Lan, 12/5/2025

description:
This program defines a circular queue class which could use for BFS.
----------------------------------------------------------------------
dynamic queue (circular buffer)
functions:
1. push(value): Add an element to the end of the queue.
2. pop(): Remove and return the element from the front of the queue.
3. count(): Return the current size of the queue.
4. display(): Return a string representation of the queue.

example usage:
from queue import Queue_circular
q = Queue_circular()
q.push(10)
q.push(20)
print(q.display())  # Output: [10, 20]  
value = q.pop()
print(value)         # Output: 10
print(q.display())  # Output: [20]
----------------------------------------------------------------------
'''
# typing
#
from typing import List, Any, Optional

# main class
#
class Queue_circular:
    # constructor
    #
    def __init__(self , buffersize:int = 10)->None:
        self.buffersize = buffersize
        self.buffer:List[Any] = [None for _ in range(buffersize)]
        self.n_elements = 0
        # initial two pointer for FIFO
        #
        self.remove_pointer = 0
        self.add_pointer = 0

    def push(self,value:Any)->None:
        # resize
        # check if the element large or equal to the buffersize
        #
        if self.n_elements >= self.buffersize:
            # double the buffer size
            #
            sec_buffersize= self.buffersize *2
            # fill the list with none
            #
            sec_buffer: List[Any] = [None for _ in range(sec_buffersize)]
            # using for loop to copy the data from the old buffer
            # start from the remove_pointer
            # to keep the order correct
            #
            for i in range(self.n_elements):
                sec_buffer[i] = self.buffer[(self.remove_pointer + i) % self.buffersize]
            # replace newbuffer to original buffer
            #
            self.buffer = sec_buffer
            self.buffersize = sec_buffersize
            # reset the pointer
            #
            self.remove_pointer = 0
            self.add_pointer = self.n_elements
        # push the value
        #
        self.buffer[self.add_pointer] = value
        # move the pointer forward and mod for circular buffer
        #
        self.add_pointer = (self.add_pointer +1) % self.buffersize
        # count increase
        #
        self.n_elements += 1

    def pop(self)->Optional[Any]:
        # pop the top value from the queue and return it. If the
        # queue is empty, return <None>
        # if list have any element
        #
        if(self.n_elements > 0):
            # assign the element in the remove_pointer in to a variable
            #
            removed:Optional[Any] = self.buffer[self.remove_pointer]
            # replace the element in remove_pointer to None
            #
            self.buffer[self.remove_pointer]= None
            # move the remove_pointer to next place
            #
            self.remove_pointer = (self.remove_pointer + 1) % self.buffersize
            # subtract 1 in number of total elements
            #
            self.n_elements -= 1
            # return the removed value
            #
            return removed
        else:
            return None

    def count(self)-> int:
        # return the number of valid elements in the queue
        # return the number of total element
        return self.n_elements
    