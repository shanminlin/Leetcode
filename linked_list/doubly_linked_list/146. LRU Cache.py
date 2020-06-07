#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
# 
# The cache is initialized with a positive capacity.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);<br>
# cache.put(2, 2);<br>
# cache.get(1);       // returns 1<br>
# cache.put(3, 3);    // evicts key 2<br>
# cache.get(2);       // returns -1 (not found)<br>
# cache.put(4, 4);    // evicts key 1<br>
# cache.get(1);       // returns -1 (not found)<br>
# cache.get(3);       // returns 3<br>
# cache.get(4);       // returns 4<br>

# # Brainstorm
# 
# - As we want to store key-value pairs, a hash table seems the right option.
# - As we also need to evict the oldest item if exceeding capacity, a queue seems helpful. The front of the queue will be LRU item and will be removed first.
# - Basically when we perform a get or put operation for a key, that key will be at the end of the queue.
# - What if we want to put a key that is already present in the cache? 
#       - the key will be updated to the new value, and the key will be at the end of the queue.
# 
# OrderedDict
# - remove: popleft(False) if FIFO
# 

# In[ ]:


from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.queue = deque()
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            # Reorder of LRU queue
            value = self.cache[key]
            self.queue.remove(key)
            self.queue.append(key)
            return value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.queue.remove(key)
            self.queue.append(key)
            
        else:
            self.cache[key] = value
            self.queue.append(key)
            
        if len(self.queue) > self.capacity:
            LRU = self.queue.popleft()
            self.cache.pop(LRU)


# # Solution 2
# ##### OrderedDict

# In[14]:


from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity      

    def get(self, key: int) -> int:
        if key in self.cache:
            # Reorder of LRU queue
            value = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            
        else:
            self.cache[key] = value
            
        if len(self.cache) > self.capacity:
            self.cache.popitem(False) 

