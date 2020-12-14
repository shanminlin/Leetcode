#!/usr/bin/env python
# coding: utf-8

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
# Solution 1
# O(N^3) time
class Solution1:
    def threeSum(self, nums):
        nums.sort()
        result = []
        temp_list = []
        self.helper(nums, temp_list, result)
        return result
    
    def helper(self, nums, temp_list, result):
        if len(temp_list) == 3 and sum(temp_list) == 0:
            result.append(temp_list)
            return
        
        elif len(temp_list) > 3 or sum(temp_list) > 0:
            return
        
        else:
            for i in range(len(nums)):
                if nums[i] == nums[i-1] and i != 0:
                    continue
                else:
                    self.helper(nums[i+1:], temp_list+[nums[i]], result)


# Solution 2
# O(N^2) time

class Solution2:
    def threeSum(self, nums):
        
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            complement = -num
            l = i + 1
            r = len(nums) - 1
            while l < r: # when l == r, stop
                if l - 1 != i and nums[l] == nums[l-1]:
                    l += 1
                    continue
                   
                if r + 1 <= len(nums) - 1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
 
                if nums[l] + nums[r] == complement:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < complement:
                    l += 1
                else:
                    r -= 1
        return result




# My wrong solution. It does not handle the case when there are two groups of two_sums. and does not handle duplicate three sums.
class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        
        three_sum = []    
        for i in range(len(nums) - 3):
            complement = 0 - nums[i]
            two_sum_elements = self.two_sum(nums[i + 1:], complement)
            if two_sum_elements:
                two_sum_elements.append(nums[i])
                three_sum += [two_sum_elements]
                
        return three_sum
    
    def two_sum(self, nums, target):
        nums_set = set()
        for num in nums:
            complement = target - num
            if complement in nums_set:
                return [complement, num]
            nums_set.add(num)

