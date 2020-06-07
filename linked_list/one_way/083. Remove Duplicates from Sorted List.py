#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# 
# Example 1:
# 
# Input: 1->1->2<br>
# Output: 1->2<br>
# 
# 
# Example 2:
# 
# Input: 1->1->2->3->3<br>
# Output: 1->2->3

# # Brainstorm
# 
# 

# # Solution

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else: 
                curr = curr.next
            
        return head

