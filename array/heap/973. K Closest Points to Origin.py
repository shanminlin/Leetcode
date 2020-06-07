#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0). (Here, the distance between two points on a plane is the Euclidean distance.) You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
# 
#  
# 
# Example 1:<br>
# Input: points = [[1,3],[-2,2]], K = 1<br>
# Output: [[-2,2]]<br>
# 
# Example 2:<br>
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2<br>
# Output: [[3,3],[-2,4]]<br>
# (The answer [[-2,4],[3,3]] would also be accepted.)

# In[ ]:


from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # min heap, but want max heap
        heap = []
        for point in points:
            distance = (point[0] ** 2 + point[1] ** 2) * (-1)
            
            if len(heap) == K:
                if heap[0][0] < distance:
                    heappop(heap)
                    heappush(heap, (distance, point))
            else:
                heappush(heap, (distance, point))
            
            
            
        return [pair[1] for pair in heap]


# The comparision if heap[0][0] < distance works unnessicary extra steps. Since we are building the heap, the building process involves comparision. The below solution gives same time and space complexity.

# In[ ]:


from heapq import heappush, heappop, heappushpop
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # min heap, but want max heap
        heap = []
        for point in points:
            distance = (point[0] ** 2 + point[1] ** 2) * (-1)
            
            if len(heap) == K:
                heappushpop(heap, (distance, point))
            else:
                heappush(heap, (distance, point))
            
            
            
        return [pair[1] for pair in heap]

