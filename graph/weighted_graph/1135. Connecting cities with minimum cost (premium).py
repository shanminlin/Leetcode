#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# There are N cities numbered from 1 to N.
# 
# You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)
# 
# Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.
# 
# <img src='./images/city1.png'>
# Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]<br>
# Output: 6<br>
# Explanation: <br>
# Choosing any 2 edges will connect all cities so we choose the minimum 2.
# 
# <img src='./images/city2.png'>
# Input: N = 4, connections = [[1,2,3],[3,4,4]]<br>
# Output: -1<br>
# Explanation:<br>
# There is no way to connect all cities even if all edges are used.
# 
# 
# Note:
# 
# 1 <= N <= 10000<br>
# 1 <= connections.length <= 10000<br>
# 1 <= connections[i][0], connections[i][1] <= N<br>
# 0 <= connections[i][2] <= 10^5<br>
# connections[i][0] != connections[i][1]<br>
