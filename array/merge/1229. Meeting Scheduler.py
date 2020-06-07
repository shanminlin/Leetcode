#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.
# 
# If there is no common time slot that satisfies the requirements, return an empty array.
# 
# The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.  
# 
# It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.
# 
#  
# 
# Example 1:
# 
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8<br>
# Output: [60,68]<br>
# 
# Example 2:
# 
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12<br>
# Output: []<br>
#  
# 
# Constraints:
# 
# 1 <= slots1.length, slots2.length <= 10^4<br>
# slots1[i].length, slots2[i].length == 2<br>
# slots1[i][0] < slots1[i][1]<br>
# slots2[i][0] < slots2[i][1]<br>
# 0 <= slots1[i][j], slots2[i][j] <= 10^9<br>
# 1 <= duration <= 10^6 

# # Brainstorm
# 
# Find overlapping time slots between the two people. 
# - later start time + duration < end time of both people
# - 

# Time limit exceed solution

# In[ ]:


class Solution:
    def minAvailableDuration(self, slots1, slots2, duration):
        
        if not slots1 or not slots2:
            return []
        
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        
        for slot1 in slots1:
            for slot2 in slots2:
                if slot1[0] <= slot2[0] < slot1[1] or slot2[0] <= slot1[0] < slot2[1]:
                    start = max(slot1[0], slot2[0])
                    meeting_end = start + duration
                    if meeting_end <= slot1[1] and meeting_end <= slot2[1]:
                        return [start, meeting_end]
                
        return []


# This does not make use of the fact that both lists are sorted.

# In[ ]:




