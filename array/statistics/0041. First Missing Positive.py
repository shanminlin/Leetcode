#!/usr/bin/env python
# coding: utf-8

"""
Problem

Given an unsorted integer array, find the smallest missing positive integer.<br>

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1
 
Note:
Your algorithm should run in O(n) time and uses constant extra space.

Brainstorm

Start with a brute force
- Sort the array.
- For the positive part of the array, compare it with a set containing 1 to max of the positive array.
- Remove numbers from the array that are also present in the set
- The smallest number in the set is now what we want.
 
First, can we reduce the search space?
- If the array is all positive from 1 to length - 1, the smallest missing positive is between 1 and n + 1.
 
Can we eliminate the set?
If the array is [5, 2, 4], the set will be just {1, 2, 3, 4}
It seems that the set is like the index of an array.
One common way to use the index to flag the presence of a number without losing the original number at that index is to use a negative sign.
To use this method, we need to convert all numbers to positive.
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # our potential candidate will be in the range between 1 and n inclusive.
        # if the list contains all numbers from 1 to n, then the result will be n+1

        # convert negative values to n+1
        n = len(nums)
        for i, num in enumerate(nums):
            if num < 1:
                nums[i] = n + 1
                
        
        # use the index to mark the presence of a number
        for i, num in enumerate(nums):
            value = abs(num)
            if value >= 1 and value <= n and nums[value-1] > 0: # if duplicates, the index is already marked, so ignore
                nums[value-1] *= -1
                
        # find the index for the first positive value
        for i, num in enumerate(nums):
            if num > 0:
                return i+1
        
        # if all indices are marked, the result will be n+1
        return n+1
