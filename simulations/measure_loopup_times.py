import matplotlib.pyplot as plt
import time
import random
import math
import sys
import os
#from DataStructures.bst import BST
from DataStructures.graph import Graph
from DataStructures.hashTable import HashTable
from DataStructures.array import array
from DataStructures.array import BucketArray

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

ns = [1, 10, 100, 1000, 10000, 100000]
array_times = []
bucket_times = []
hash_times = []
#bst_times = []

for n in ns:
    # For array
    arr = array()
    for i in range(len(ns)):
        arr.append(i)
    
    # Measure lookup time for all elements
    start_time = time.perf_counter()
    for i in range(len(ns)):
        _ = arr.get(i)
    end_time = time.perf_counter()
    
    avg_time = (end_time - start_time) / len(ns)
    array_times.append(avg_time)

    # Test BucketArray
    bucket_arr = BucketArray(bucket_capacity=10)
    for i in range(len(ns)):
        bucket_index = i // 10  # each bucket has 10 elements
        bucket_arr.add_to_bucket(bucket_index, i)
    
    # Measure lookup time: traverse each bucket and element
    start_time = time.perf_counter()
    for i in range(bucket_arr.size()):
        bucket = bucket_arr.get_bucket(i)
        if bucket:
            for j in range(bucket.size()):
                _ = bucket.get(j)
    end_time = time.perf_counter()
    
    avg_time_bucket = (end_time - start_time) / len(ns)
    bucket_times.append(avg_time_bucket)

    # For Hash table
    ht = HashTable(size=5000)
    keys = random.sample(range(n*10), n)
    
    # Insert keys into hash table
    for key in keys:
        ht.insert(key, random.randint(1, 1000))
    
    # Measure lookup time
    start_time = time.perf_counter()
    for key in keys:
        ht.lookup(key)
    end_time = time.perf_counter()
    
    avg_lookup_time = (end_time - start_time) / len(ns)
    hash_times.append(avg_lookup_time)


plt.figure(figsize=(8,5))
plt.plot(ns, array_times, 'r-o', label='array')
plt.plot(ns, bucket_times, 'g-o', label='BucketArray')
plt.plot(ns, hash_times, 'y-o', label = 'HashTable')
#plt.plot(ns, bst_times, 'b-o', label = "BST")
plt.title("Lookup time (n)")
plt.xlabel("N")
plt.ylabel("Average Lookup Time (seconds)")
plt.grid(True)
plt.legend()
plt.savefig("array_insert.pdf")
plt.show()