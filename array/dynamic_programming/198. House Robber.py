#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
# 
# Example 1:
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:
# 
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.

# # Solution 1
# ##### Recursion with list slicing

# In[ ]:


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        
        max_amount = max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        return max_amount


# # Solution 2
# ##### Recursion with list indexing

# In[ ]:


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        curr_index = 0
        return self.recurse(nums, curr_index)
    
    def recurse(self, nums, curr_index):
        
        if curr_index == len(nums) - 1:
            return nums[curr_index]
        elif curr_index == len(nums) - 2:
            return max(nums[len(nums) - 1], nums[len(nums) - 2])
        
        max_amount = max(nums[curr_index] + self.recurse(nums, curr_index + 2), self.recurse(nums, curr_index + 1))
        return max_amount


# # Solution 3
# ##### Recursion with memoization

# In[ ]:


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        length = len(nums)
        memo = {length - 1: nums[length - 1], length - 2: max(nums[length - 1], nums[length - 2])}
        
        curr_index = 0
        return self.recurse(nums, curr_index, memo)
    
    def recurse(self, nums, curr_index, memo):
        
        if curr_index == len(nums) - 1 or curr_index == len(nums) - 2 or curr_index in memo:
            return memo[curr_index]
        
      
        memo[curr_index] = max(nums[curr_index] + self.recurse(nums, curr_index + 2, memo), self.recurse(nums, curr_index + 1, memo))
            
        return memo[curr_index]

