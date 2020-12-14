#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times. <br>
# 
# You may assume that the array is non-empty and the majority element always exist in the array.<br>
# 
# Example 1:<br>
# 
# Input: [3,2,3]<br>
# Output: 3<br>
# 
# Example 2:<br>
# 
# Input: [2,2,1,1,1,2,2]<br>
# Output: 2

# # Solution 1
# ##### Hash table 


from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums_dict = Counter(nums)
        threshold = len(nums) // 2 + 1
        
        for num, count in nums_dict.items():
            if count >= threshold:
                return num


# # Solution 2
# ##### Sort 


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()
        return nums[len(nums) // 2]
                


# # Solution 3
# ##### Boyer-Moore Voting Algorithm
# This is to find the majority element. To check whether the majority element is occurring more than n/2 times, we still need a hashtable to count.


class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
                
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate