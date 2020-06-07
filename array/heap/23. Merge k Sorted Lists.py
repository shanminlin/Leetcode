#!/usr/bin/env python
# coding: utf-8

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# 
# Example:
# 
# Input:<br>
# 1->4->5<br>
# 1->3->4<br>
# 2->6<br>
# Output:<br>
# 1->1->2->3->4->4->5->6

# 1. Clarify the question
# 
# So we are given k linked lists, which are sorted, and we need to return one sorted linked list.
# 
# Assumptions: - duplicate values?

# 2. Input and output

# 3. test cases and edge cases

# 4. Brainstorming
# 
# If we just want to merge 2 linked lists, think of merge sort. we can just compare Node1 and Node2
# 
# But if we want to generalize to k linked lists, how to make the comparison?
# 
