"""
linkedlist.py

purpose: Used throughout the movie database project as a core data structure, have to use it in hash table data structure 
            since built-ins are not allowed
"""
class LinkedList:
    # linked list used for storing (key, value) pairs

    # inner node class
    class Node:
        def __init__(self, key=None, value=None, next=None):
            self.key = key
            self.value = value
            self.next = next

    # initialization
    def __init__(self):
        self.head = None

    # insert new node 
    def insert(self, key, value):
        # insert at the head of the list. If the key already exists, update

        curr = self.head
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        new_node = self.Node(key, value, self.head)
        self.head = new_node

    # lookup
    def lookup(self, key):
        # finds and return the value associated, returns None if key not found
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None
    
    # remove node
    def remove(self, key):
        # remove node with matching key. Returns true if removed, false if key not found
        prev = None
        curr = self.head

        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev, curr = curr, curr.next
        return False
    
    def __iter__(self):
        curr = self.head
        while curr:
            yield (curr.key, curr.value)
            curr = curr.next
    
    # display method
    def display(self):
        # print linked list contents
        curr = self.head
        if not curr:
            print("Empty List")
            return
        while curr:
            print(f"[{curr.key}: {curr.value}] -> ", end="")
            curr = curr.next
        print("None")