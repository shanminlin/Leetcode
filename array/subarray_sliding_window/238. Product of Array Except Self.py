#!/usr/bin/env python
# coding: utf-8

# # 238. Product of Array Except Self
# 
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# 
# Example:
# Input:  [1,2,3,4]<br>
# Output: [24,12,8,6]<br>
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

# # Brainstorm
# 
# For each number, we compute the product of the elements on its left through iterating the indices, and the product of the elements on its right through iteration. Then times the two products.
# - Time O(N^2). Space O(N) to store the product array.
# 
# Can we reduce the time? Then we have to think of ways to store the products along the way. And probably we have to do multiple iterations.
# 

# # Solution 1
# ##### left and right product arrays

# In[ ]:


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        
        length = len(nums)
        left_products = [1] * length
        right_products = [1] * length
        
        # Compute products to the left of nums[i]
        for i in range(1, length):
            left_products[i] = left_products[i-1] * nums[i-1]
        
        # Similarly, compute products to the right of nums[j]
        for j in range(length-2, -1, -1):
            right_products[j] = right_products[j+1] * nums[j+1]
            
            
        products = [left * right for left, right in zip(left_products, right_products)]
        
        return products


# # Solution 2
# ##### left product array and right product variable

# In[ ]:


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        
        length = len(nums)
        products = [1] * length

        # Compute products to the left of nums[i]
        for i in range(1, length):
            products[i] = products[i-1] * nums[i-1]
        
        
        right_product = 1
        for j in range(length-2, -1, -1):
            right_product *= nums[j+1]
            products[j] *= right_product
        
        return products

