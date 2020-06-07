#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.
# 
# 
# Example 1:
# 
# Input: arr = [1,2,3,4,5], k = 4, x = 3<br>
# Output: [1,2,3,4]<br>
# 
# Example 2:
# 
# Input: arr = [1,2,3,4,5], k = 4, x = -1<br>
# Output: [1,2,3,4]<br>
#  
# 
# Constraints:
# 
# 1 <= k <= arr.length<br>
# 1 <= arr.length <= 10^4<br>
# Absolute value of elements in the array and x will not exceed 10^4

# # Brainstorm
# 
# Calculate the difference between elements and x, then sort the differences in ascending order, take the first k
# - Time O(NlogN), space O(N)
# 
# Use a heap of size k
# - Time O(NLogN), space O(k)
# 
# Use binary search to find the closet, then add elements around it until k
# - Time O(LogN + k), space O(k)

# In[ ]:


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 1:
            return arr

        # Binary search to find last two elements
        low = 0
        high = len(arr) - 1
        while high - low > 1:
            mid = (high + low) // 2
            mid_num = arr[mid]

            if x >= mid_num:
                low = mid
            else:
                high = mid
            
        # We have two elements from previous search
        # need to find the closer one
        closest_num_index = 0
        if abs(arr[low] - x) <= abs(arr[high] - x):
            closest_num_index = low
        else:
            closest_num_index = high
            
        # Special case 
        if k == 1:
            return [arr[closest_num_index]]
        
        left = closest_num_index - 1
        right = closest_num_index + 1
        count = 1
        while count < k:
            if left < 0:
                right += 1
                count += 1
            elif right == len(arr):
                left -= 1
                count += 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                count += 1
                left -= 1
            else:
                count += 1
                right += 1
        
        if left < 0:
            left = -1
        
        return arr[left+1:right]

