#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a linked list, determine if it has a cycle in it.

# # Brainstorm
# 
# Traverse the linked list, and keep track of the visited nodes using a set.
# - If current node is in the set, there is a cycle.
# - Time O(N), space O(N).
# 
# Can we reduce the space or time? 
# - If you have not seen the Floyd's cycle detection algorithm, ......
# - Based on the above mentioned algorithm, use slow and fast pointers.
# - Slow pointer moves 1 step at a time, fast pointer moves 2 steps at a time.
# - This is equivalent to slow pointer being stagnant, while fast pointer moves 1 step at a time. If there is a cycle, fast pointer will meet slow pointer.
# - If no cycle, fast pointer will reach Null first.
# - Time O(N), space O(1)

# # Solution 1
# ##### Set

# In[1]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        
        nodes = set()
        
        while head:
            if head in nodes:
                return True
            nodes.add(head)
            head = head.next
            
        return False


# # Solution 2
# ##### Two pointers 

# In[2]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        
        slow = head
        fast = head
        
        while fast.next is not None and fast.next.next is not None:
            
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
            
        return False

