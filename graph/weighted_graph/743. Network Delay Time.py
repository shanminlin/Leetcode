#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# There are N network nodes, labelled 1 to N.
# 
# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
# 
# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
# 
# <img src='./images/network.png'>
# 
# 
# Note:
# N will be in the range [1, 100].<br>
# K will be in the range [1, N].<br>
# The length of times will be in the range [1, 6000].<br>
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.<br>

# # Brainstorm
# 
# We are given weight between any two possible edges. We need a way to compute the accumulated weight from the start node to any node.

# # Solution 1
# ##### BFS

# In[ ]:


from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        graph = {}
        
        for parent, child, time in times:
            if parent not in graph:
                graph[parent] = []
            graph[parent].append((child, time))
            
        visited = set()
        queue = deque([(K, 0)])
        total_time = 0
        
        while queue:
            level_time = 0
            for _ in range(len(queue)):
                vertex, time = queue.popleft()
                visited.add(vertex)
                level_time = max(time, level_time)
                
                if vertex in graph:
                    for child, time in graph[vertex]:
                        if child not in visited:
                            queue.append((child, time))
                        
            total_time += level_time
                        
        if len(visited) < N:
            return -1
        else:
            return total_time

