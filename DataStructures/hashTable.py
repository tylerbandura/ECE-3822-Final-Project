"""
hashtable.py

purpose: used in the project to store and search movie data by keys such as title, ID, or genre

"""
from DataStructures.linkedlist import LinkedList

class HashTable:
    # hash map that uses linked lists to prevent collistions
    def __init__(self, size=50):
        self.size = size
        self.buckets = [LinkedList() for _ in range(size)]

    # custom hash function
    def _hash_function(self, key):
        # compute a hash index for a given key
        # works for both strings and integers

        if isinstance(key, int):
            return key % self.size
        
        # for strings, sum of ASCII * position index
        total = 0
        for i, ch in enumerate(str(key)):
            total += ord(ch) * (i + 1)
        return total % self.size
    
    # core operations
    def insert(self, key, value):
        index = self._hash_function(key)
        self.buckets[index].insert(key, value)

    def lookup(self, key):
        index = self._hash_function(key)
        return self.buckets[index].lookup(key)
    
    def remove(self, key):
        index = self._hash_function(key)
        return self.buckets[index].remove(key)
    
    def display(self):
        for i, bucket in enumerate(self.buckets):
            items = list(bucket)
            if items: 
                print(f"Bucket {i}: {items}")