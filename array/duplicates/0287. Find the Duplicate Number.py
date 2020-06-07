#!/usr/bin/env python
# coding: utf-8

# # Problem 
# 
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.<br>
# 
# Example 1:<br>
# 
# Input: [1,3,4,2,2]<br>
# Output: 2<br>
# 
# Example 2:<br>
# 
# Input: [3,1,3,4,2]<br>
# Output: 3<br>
# 
# Note:<br>
# You must not modify the array (assume the array is read only).<br>
# You must use only constant, O(1) extra space.<br>
# Your runtime complexity should be less than O(n2).<br>
# There is only one duplicate number in the array, but it could be repeated more than once.

# # Brainstorm
# hash table and sorting solutions do not meet the requirement.
# Floyd's Tortoise and Hare (Cycle Detection). This is very hard to think of if you have not seen the problem before. And it has very strict conditions for its use case here: only 1 duplicate, the values of the numbers are constrained by the indices.<br><br>
# How to represent the link between numbers as required by the tortoise and hare algorithm?
# 

# # Solution

# In[ ]:


class Solution:
    def findDuplicate(self, nums):
        if not nums:
            return 0
        
        # Assume there is a dummy head 0 
        # so slow = head.next
        # fast = head.next.next
        # this step is to make the ending condition 
        # of the following while loop to be false 
        # so the loop can run
        slow = nums[0] 
        fast = nums[nums[0]]
        
        while slow != fast:
            # slow moves 1 step forward
            slow = nums[slow]
            # fast moves 2 steps forward
            fast = nums[nums[fast]]
        
        # Important: remember we have a dummy head
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow


# If we don't want the dummy head:

# In[ ]:


class Solution:
    def findDuplicate(self, nums):
        if not nums:
            return 0
        
        slow = nums[0] 
        fast = nums[0]
        
        while True:
            # slow moves 1 step forward
            slow = nums[slow]
            # fast moves 2 steps forward
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

