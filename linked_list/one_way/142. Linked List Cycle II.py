#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# 
# Note: Do not modify the linked list. 
# 
# Follow-up:
# Can you solve it without using extra space?

# # Brainstorm
# 
# If we keep track of visited nodes as we traverse the linked list:
# - Time O(N), space O(N)
# 
# Can we reduce time or space?
# - If you don't know Floyd's algorithm, ..... 
# - Now assume that we know when the two pointers meet, the steps to the cycle starting node from the meeting point is the same as that from the head.
# - Find the node where a pointer from head and a pointer from the meeting point meets.
# - Time O(N), space O(1).

# # Solution 1
# ##### Set

# In[1]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(head):
        if head is None or head.next is None:
            return None
        
        seen = set()
        
        curr = head
        
        while curr:
            if curr in seen:
                return curr
            
            seen.add(curr)
            curr = curr.next
            
        return None


# # Solution 2
# ##### Two pointers

# In[2]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(head):
        
        if head is None or head.next is None:
            return None
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow2 = head
                while slow2 != slow:
                    slow2 = slow2.next
                    slow = slow.next
                return slow
                
            
        return None

