#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.
# 
# A critical connection is a connection that, if removed, will make some server unable to reach some other server.
# 
# Return all critical connections in the network in any order.
# 
# <img src='../images/critical.png'>
# 
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]<br>
# Output: [[1,3]]<br>
# Explanation: [[3,1]] is also accepted.<br>
#  
# 
# Constraints:<br>
# 
# 1 <= n <= 10^5<br>
# n-1 <= connections.length <= 10^5<br>
# connections[i][0] != connections[i][1]<br>
# There are no repeated connections.
