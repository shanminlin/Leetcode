#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
# 
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
# 
# Example 1:<br>
# Input: flowerbed = [1,0,0,0,1], n = 1<br>
# Output: True<br>
# 
# Example 2:<br>
# Input: flowerbed = [1,0,0,0,1], n = 2<br>
# Output: False<br>
# 
# Note:
# The input array won't violate no-adjacent-flowers rule.<br>
# The input array size is in the range of [1, 20000].<br>
# n is a non-negative integer which won't exceed the input array size.

# # Brainstorm
# 
# Always plant from the earliest available spot. This is a greedy solution.

# In[ ]:


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        # Special cases
        if n == 0:
            return True
        if not flowerbed:
            return False
        if len(flowerbed) == 1:
            if flowerbed[0] == 1 or n > 1:
                return False
            else:
                return True
        
        # Find nearest possible spot and plant
        for i in range(len(flowerbed)-1):
            if i == 0 and flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
            elif flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                i += 2
                n -= 1
            if n == 0:
                return True
                
        
        # We have not checked the last spot yet        
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
            if n == 0:
                return True
            
        return False

