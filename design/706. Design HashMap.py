#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Design a HashMap without using any built-in hash table libraries.
# 
# To be specific, your design should include these functions:
# 
# put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.
# 
# Example:
# 
# MyHashMap hashMap = new MyHashMap();<br>
# hashMap.put(1, 1); <br>         
# hashMap.put(2, 2); <br>        
# hashMap.get(1);            // returns 1<br>
# hashMap.get(3);            // returns -1 (not found)<br>
# hashMap.put(2, 1);          // update the existing value<br>
# hashMap.get(2);            // returns 1 <br>
# hashMap.remove(2);          // remove the mapping for 2<br>
# hashMap.get(2);            // returns -1 (not found) <br>
# 
# Note:
# 
# All keys and values will be in the range of [0, 1000000].<br>
# The number of operations will be in the range of [1, 10000].<br>
# Please do not use the built-in HashMap library.

# # Brainstorm
# 
# - Design a hash function
#        - hash function: key mod n will give the index for the value.
#        - table size n: prime number to reduce collion
# - How to handle collion?
#        - separate chaining: using an array or linked list to store values with the same hash code (key mod n)
#      
# - more about inital capacity, load factor and rehashing:
#        - if the default table size is 10 (10 buckets) and load factor is 70%, this means the maximum number of data in the hash table is 7. Then if we want to add the 8th item, the table size doubles to 20.

# # Solution

# In[ ]:


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table_size = 2069
        self.hash_table = [Bucket() for _ in range(self.table_size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_code = key % self.table_size
        self.hash_table[hash_code].update(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_code = key % self.table_size
        return self.hash_table[hash_code].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_code = key % self.table_size
        self.hash_table[hash_code].remove(key)
        
        
class Bucket:
    def __init__(self):
        self.bucket = []
    
    def update(self, key, value):
        key_found = False
        for i, (k, v) in enumerate(self.bucket):
            if key == k:
                self.bucket[i] = key, value
                key_found = True
                break
        if not key_found:
            self.bucket.append((key, value))
    
    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1
    
    def remove(self, key):
        for k, v in self.bucket:
            if k == key:
                self.bucket.remove((k, v))
            

