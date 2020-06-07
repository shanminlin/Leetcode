#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a sorted integer array without duplicates, return the summary of its ranges.
# 
# Example 1:<br>
# 
# Input:  [0,1,2,4,5,7]<br>
# Output: ["0->2","4->5","7"]<br>
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.<br>
# 
# Example 2:
# 
# Input:  [0,2,3,4,6,8,9]<br>
# Output: ["0","2->4","6","8->9"]<br>
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

# # Brainstorm
# 
# This problem is very prone to off-by-one error.
# - Time O(N)
# - space O(N)

# In[ ]:


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        summary = []
        i = 0
        while i < len(nums):
            start_num = nums[i]
            
            while i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
                i += 1
            
            if start_num != nums[i]:
                s = str(start_num) + '->' + str(nums[i])
            else:
                s = str(start_num)
            
            i += 1
            summary.append(s)
        return summary

