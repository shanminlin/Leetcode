#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.<br>
# 
# Example 1:<br>
# Input: [[0, 30],[5, 10],[15, 20]]<br>
# Output: 2<br>
# 
# Example 2:<br>
# Input: [[7,10],[2,4]]<br>
# Output: 1<br>

# # Brainstorm
# 
# If we sort the meetings based on start time, there are several scenarios:
# - the next meeting does not overlap with the previous meeting, so we don't need to allocate a new room.
# - the next meeting overlaps with the previous meeting, and there is only 1 meeting happening, we will allocate a new room.
# - the next meeting overlaps with the previous meeting, but an even earlier meeting has ended, then we don't allocate a new room.
# - the next meeting overlaps with the previous meeting, all earlier meetings have not ended, then we will allocate a new room.
# 
# So we need to keep track of previous meetings' ending time and check an earlier ending meeting and compare it with the current meeting, a min heap could help to reduce time complexicity from O(N^2) to O(N Log N). heap push take logN time. So using heap, the time is dominated by sorting which is O(NlogN). Space is O(N), same as an array.
# 

# # Solution

# In[ ]:


import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        
        # Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])
        
        room_heap = []
        heapq.heappush(room_heap, (intervals[0][1], intervals[0][0])) 
        room_count = 1
        
        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            prev_end = intervals[i-1][1]
            
            # If two meetings overlap
            if curr_start < prev_end:
                # Check if any earlier meeting has ended
                earliest_end_meeting = room_heap[0]
                earliest_end = earliest_end_meeting[0]
                
                # If got a meeting ended
                if curr_start >= earliest_end:
                    heapq.heappushpop(room_heap, (intervals[i][1], intervals[i][0]))
                else:
                    # no meeting ended
                    # allocate a new room
                    # add to room heap
                    room_count += 1
                    heapq.heappush(room_heap, (intervals[i][1], intervals[i][0]))
            
            # If two meetings do not overlap
            # Use the same meeting room as previous meeting
            # So the room in heap of previous meeting changed 
            # to current meeting time
            else:
                heapq.heappushpop(room_heap, (intervals[i][1], intervals[i][0]))
        
        return room_count


# Simplify the code:

# In[ ]:


import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])
        
        room_heap = []
        heapq.heappush(room_heap, intervals[0][1]) 
        room_count = 1
        
        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            prev_end = intervals[i-1][1]
            
            # If two meetings overlap
            if curr_start < prev_end:
                # Check if any earlier meeting has ended
                earliest_end = room_heap[0]
                
                # If got a meeting ended
                if curr_start >= earliest_end:
                    heapq.heappushpop(room_heap, intervals[i][1])
                else:
                    # no meeting ended
                    # allocate a new room
                    # add to room heap
                    room_count += 1
                    heapq.heappush(room_heap, intervals[i][1])
            
            # If two meetings do not overlap
            # Use the same meeting room as previous meeting
            # So the room in heap of previous meeting changed 
            # to current meeting time
            else:
                heapq.heappushpop(room_heap, intervals[i][1])
        
        return room_count

