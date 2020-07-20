#!/usr/bin/env python
# coding: utf-8

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

# sliding window
# time O(N), space O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_sum = float('-inf')
        curr_sum = 0
        for num in nums:
            # compute sum for previous subarray
            curr_sum += num
            
            # if current sum <= the current number,
            # no need to include previous subarray
            if curr_sum <= num:
                curr_sum = num
                
            max_sum = max(max_sum, curr_sum)  
        return max_sum