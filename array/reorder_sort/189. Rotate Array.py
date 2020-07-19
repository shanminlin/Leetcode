#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array, rotate the array to the right by k steps, where k is non-negative.
# 
# Follow up:<br>
# 
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?<br>
#  
# 
# Example 1:<br>
# 
# Input: nums = [1,2,3,4,5,6,7], k = 3<br>
# Output: [5,6,7,1,2,3,4]<br>
# Explanation:<br>
# rotate 1 steps to the right: [7,1,2,3,4,5,6]<br>
# rotate 2 steps to the right: [6,7,1,2,3,4,5]<br>
# rotate 3 steps to the right: [5,6,7,1,2,3,4]<br>
# 
# 
# Example 2:<br>
# 
# Input: nums = [-1,-100,3,99], k = 2<br>
# Output: [3,99,-1,-100]<br>
# Explanation: <br>
# rotate 1 steps to the right: [99,-1,-100,3]<br>
# rotate 2 steps to the right: [3,99,-1,-100]<br>
#  
# 
# Constraints:
# 
# 1 <= nums.length <= 2 * 10^4<br>
# It's guaranteed that nums[i] fits in a 32 bit-signed integer.<br>
# k >= 0<br>

# # Brainstorm
# 
# List slicing and concatenation
# - Time O(1), space O(N)
# 
# Swap, like buble sort
# - Time O(N^2), space O(1)
# 
# In O(N) time or O(kN) time? ...

# # Solution 1
# ##### List slicing and concatenation

# In[2]:


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if not nums:
            return nums
        
        # In case k is 100000000000
        length = len(nums)
        if k >= length:
            k %= length
        
        if k == 0:
            return nums
        
        # nums[:] returns a reference to the same object
        nums[:] = nums[length-k:] + nums[:length-k]        


# # Solution 2
# ##### swap

# In[6]:


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if not nums:
            return nums
        
        length = len(nums)
        if k >= length:
            k %= length
        
        if k == 0:
            return nums
        
        swap_until = 0
        for num_to_rotate_index in range(length-k, length):
            for i in range(num_to_rotate_index, swap_until, -1):
                nums[i], nums[i-1] = nums[i-1], nums[i]
            swap_until += 1
            
        return nums


# In[7]:


s = Solution()
nums = [1, 2, 3, 4, 5]
k = 3
print(s.rotate(nums, k))


# In[ ]:




