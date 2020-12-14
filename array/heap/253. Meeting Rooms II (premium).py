#!/usr/bin/env python
# coding: utf-8

"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example, Given [[0, 30],[5, 10],[15, 20]], return 2.

"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort()
        ending_queue = []
        rooms = 0
        for i in range(1, len(intervals)):
            pre_meeting = intervals[i-1]
            cur_meeting = intervals[i]
            
            heapq.heappush(ending_queue, pre_meeting[1])
            
            if cur_meeting[0] < ending_queue[0]:
                rooms += 1
            else:
                heapq.heappop(ending_queue)
        return rooms
                


