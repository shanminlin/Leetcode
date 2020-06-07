#!/usr/bin/env python
# coding: utf-8

# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:<br>
# Input: nums = [1,1,1,2,2,3], k = 2<br>
# Output: [1,2]<br>
# 
# Example 2:<br>
# Input: nums = [1], k = 1<br>
# Output: [1]<br>
# 
# Note:
# - You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# - Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# In[ ]:


from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        top_k = count.most_common(k)
        
        result = []
        for item in top_k:
            result.append(item[0])
            
        return result


# most_common use heap
