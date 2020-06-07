#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Design a data structure that supports all following operations in average O(1) time.
# 
# insert(val): Inserts an item val to the set if not already present.<br>
# remove(val): Removes an item val from the set if present.<br>
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.<br>
# 
# Example:
# 
# // Init an empty set.<br>
# RandomizedSet randomSet = new RandomizedSet();<br>
# 
# // Inserts 1 to the set. Returns true as 1 was inserted successfully.<br>
# randomSet.insert(1);<br>
# 
# // Returns false as 2 does not exist in the set.<br>
# randomSet.remove(2);<br>
# 
# // Inserts 2 to the set, returns true. Set now contains [1,2].<br>
# randomSet.insert(2);<br>
# 
# // getRandom should return either 1 or 2 randomly.<br>
# randomSet.getRandom();<br>
# 
# // Removes 1 from the set, returns true. Set now contains [2].<br>
# randomSet.remove(1);<br>
# 
# // 2 was already in the set, so return false.<br>
# randomSet.insert(2);<br>
# 
# // Since 2 is the only number in the set, getRandom always return 2.<br>
# randomSet.getRandom();<br>

# # Brainstorm
# 
# A set allows insert and remove at average and amortized O(1) time. However, it doesn't allow random sampling of elements. set.pop() does not remove in a random manner. After Python 3.6, it removes the first element added.<br>
# 
# To pick a random integer between a and b inclusive, there are three options:
# - n = random.randint(0, 2)
# - n = random.choice([0, 1, 2])
# 
# Therefore, we need an index to identify each element in the set. So a dictionary with key as the , 
# - How to assign a number to an element that we inserted
# - adding a class attribute that is incremented each time we call insert() does not work as the range of values 

# # Solution

# In[ ]:


import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict:
            # Insert to dict
            self.dict[val] = len(self.array)
            # Insert to array
            self.array.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # swap element with last element in array
            # remove last element in array
            index = self.dict[val]
            last_element = self.array[-1]
            self.array[index], self.array[-1] = self.array[-1], self.array[index]
            self.array.pop()
            # update index for the original last element
            self.dict[last_element] = index
            
            # remove from dict
            del self.dict[val]
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.array)

