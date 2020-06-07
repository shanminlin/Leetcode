#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
# 
# Example 1:<br>
# Input:nums = [1,1,1], k = 2<br>
# Output: 2<br>
# 
# Note:
# - The length of the array is in range [1, 20,000].
# - The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

# # Brainstorm
# 
# Duplicates
# 
# Brute force: have to check every subarray, because -ve number is possible. If the current sum > k, still needs to go on to check.
# 
# current_subarray_sum - k:
# - what if same subarray_sum multiple times.

# In[ ]:


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        for i in range(len(nums)):
            curr_sum = nums[i]
            if curr_sum == k:
                count += 1

            for j in range(i+1, len(nums)):
                curr_sum += nums[j]
                if curr_sum == k:
                    count += 1

        return count


# In[ ]:


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        subarray_sum = {0: 1}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in subarray_sum:
                count += subarray_sum[curr_sum - k]
            subarray_sum[curr_sum] = subarray_sum.get(curr_sum, 0) + 1
        return count


# Wrong solution:

# In[ ]:


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        subarray_sum = {0: 1}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in subarray_sum:
                count += 1
            subarray_sum[curr_sum] = subarray_sum.get(curr_sum, 0) + 1
        return count

