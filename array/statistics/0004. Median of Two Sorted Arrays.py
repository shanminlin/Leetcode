#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# Example 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5

# # Brainstorm
# 

# Approach 1: Brute force
# The brute force solution is to merge the two arrays and find the middle elements for odd length, or the average of the two middle elements for even length array.

# In[3]:


def find_median_sorted_arrays(nums1, nums2):
    merged = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2): 
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1


    if i < len(nums1):
        merged.extend(nums1[i:])
    if j < len(nums2):
        merged.extend(nums2[j:])

    # find median of merged array
    if len(merged) % 2 == 0:
        median_merged = (merged[int(len(merged) / 2 - 1)] + merged[int(len(merged) / 2)]) / 2
    else:
        median_merged = merged[int(len(merged) // 2)]

    return median_merged


# In[4]:


find_median_sorted_arrays([1, 3], [2])


# Approach 2:
# - How to reduce the time complexity to O of log time.
# 
# 
