#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
# 
# Example 1:<br>
# 
# Input: [[0,30],[5,10],[15,20]]<br>
# Output: false<br>
# 
# Example 2:<br>
# 
# Input: [[7,10],[2,4]]<br>
# Output: true

# # Brainstorm
# 
# Greedy approach:
# - Take meeting with earlist starting time
# - If overlap, return False
# - Time: NlogN for sorting, N for comparison of slot pairs, overall O(NlogN)
# - Space: O(1).

# In[ ]:


class Solution:
    def canAttendMeetings(self, intervals):
        if not intervals:
            return True
        
        # Sort based on start time
        intervals.sort(key=lambda x: x[0])
        
        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            prev_end = intervals[i-1][1]
            
            # If previous slot ending time is later 
            # than current slot starting time
            if prev_end > curr_start:
                # There is overlap
                return False
        return True

