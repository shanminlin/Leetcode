#!/usr/bin/env python
# coding: utf-8

"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""

# Solution 1
# set, time O(N), space O(N)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))
    

# Solution 2
# time O(NlogN), space O(1) ignore the space to store the output 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersection = []
        i1 = 0
        i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            
            value1 = nums1[i1]
            value2 = nums2[i2]
            
            if value1 == value2:
                intersection.append(value1)
                while i1 < len(nums1) and nums1[i1] == value1:
                    i1 += 1
                while i2 < len(nums2) and nums2[i2] == value2:
                    i2 += 1
                    
            elif value1 > value2:
                # increment i2 until duplicates skipped
                while i2 < len(nums2) and nums2[i2] == value2:
                    i2 += 1
            else:
                while i1 < len(nums1) and nums1[i1] == value1:
                    i1 += 1
        return intersection
