#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.<br>
# 
# We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.<br>
# 
# Example:<br>
# Input:<br>
# routes = [[1, 2, 7], [3, 6, 7]]<br>
# S = 1<br>
# T = 6<br>
# Output: 2<br>
# Explanation:<br>
# The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
#  
# 
# Constraints:<br>
# 1 <= routes.length <= 500.<br>
# 1 <= routes[i].length <= 10^5.<br>
# 0 <= routes[i][j] < 10 ^ 6.
