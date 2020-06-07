#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be changed.
# 
#  
# 
# Example:
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# # Brainstorm
# 
# 

# # Solution

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head or head.next is None:
            return head
        
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = prev.next
        next_node = curr.next
        
        while curr is not None and curr.next is not None:
            prev.next = curr.next
            
            curr.next = next_node.next
            
            next_node.next = curr
            
            # next iteration
            prev = curr
            curr = curr.next
            if curr:
                next_node = curr.next
                
        
        return dummy.next

