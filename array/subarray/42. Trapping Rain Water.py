#!/usr/bin/env python
# coding: utf-8

# # 42. Trapping Rain Water
# 
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# <img src='./images/rainwatertrap.png'>
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
# 
# Example:<br>
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]<br>
# Output: 6

# # Brainstorm
# 
# Two pointers left and right from both ends
# - If height at left is smaller than height at right, we calculate water from left; we also move left pointer because the water is limited by lower bar. (imagine all middle bars removed).
# - we calculate area above each bar. 

# # Solution 1
# ##### histogram

# In[ ]:


def findWater(arr, n): 
  
    # left[i] contains height of tallest bar to the 
    # left of i'th bar including itself 
    left = [0]*n 
  
    # Right [i] contains height of tallest bar to 
    # the right of ith bar including itself 
    right = [0]*n 
  
    # Initialize result 
    water = 0
  
    # Fill left array 
    left[0] = arr[0] 
    for i in range( 1, n): 
        left[i] = max(left[i-1], arr[i]) 
  
    # Fill right array 
    right[n-1] = arr[n-1] 
    for i in range(n-2, -1, -1): 
        right[i] = max(right[i+1], arr[i]); 
  
    # Calculate the accumulated water element by element 
    # consider the amount of water on i'th bar, the 
    # amount of water accumulated on this particular 
    # bar will be equal to min(left[i], right[i]) - arr[i] . 
    for i in range(0, n): 
        water += min(left[i],right[i]) - arr[i] 
  
    return water 


# # Solution 2
# ##### two pointers

# In[ ]:


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        left_max = 0
        right_max = 0
        area = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            if left_max < right_max:
                left_area = left_max - height[left]
                area += left_area
                left += 1
            
            else:
                right_area = right_max - height[right]
                area += right_area
                right -= 1
        
        return area

