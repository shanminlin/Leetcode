#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
# 
# Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
# 
# <img src='images/flights.png'>
# 
# Note:
# - The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
# - The size of flights will be in range [0, n * (n - 1) / 2].
# - The format of each flight will be (src, dst, price).
# - The price of each flight will be in the range [1, 10000].
# - k is in the range of [0, n - 1].
# - There will not be any duplicated flights or self cycles.

# # Brainstorm
# 
# 

# # Solution 1
# ##### BFS (time limit exceed)

# In[ ]:


from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        
        graph = {}
        for parent, child, cost in flights:
            if parent not in graph:
                graph[parent] = []
            graph[parent].append((child, cost))
            
        
        queue = deque([(src, 0, 0)])
        
        cost_table = [[float('inf'), 0] for _ in range(n)]
        
        while queue:
            node, costs, stops = queue.popleft()
            
            if stops > K + 1:
                continue
                
            if costs < cost_table[node][0]:
                cost_table[node][0] = costs
                cost_table[node][1] = stops
                
            if node in graph and node != dst: # the node may not be a parent
                for child, cost in graph[node]:
                    queue.append((child, cost+cost_table[node][0], 1+cost_table[node][1]))
                
            
        if cost_table[dst][0] == float('inf'):
            return -1
        else:
            return cost_table[dst][0]

