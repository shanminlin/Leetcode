#!/usr/bin/env python
# coding: utf-8

# # 56. Merge Intervals
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:<br>
# Input: [[1,3],[2,6],[8,10],[15,18]]<br>
# Output: [[1,6],[8,10],[15,18]]<br>
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# 
# Example 2:<br>
# Input: [[1,4],[4,5]]<br>
# Output: [[1,5]]<br>
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# # Brainstorm
# 
# sort with start time, then merge 2nd with 1st, they become the first, then merge with the next, until last one.

# In[8]:


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if merged[-1][0] <= intervals[i][0] <= merged[-1][1]:
                merged[-1] = [merged[-1][0], max(intervals[i][1], merged[-1][1])]
            else:
                merged.append(intervals[i])
                
        return merged

