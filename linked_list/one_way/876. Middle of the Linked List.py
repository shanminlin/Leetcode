#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.<br>
# 
# If there are two middle nodes, return the second middle node.<br>
# 
#  Example 1:<br>
# 
# Input: [1,2,3,4,5]<br>
# Output: Node 3 from this list (Serialization: [3,4,5])<br>
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).<br>
# 
# Note that we returned a ListNode object ans, such that:<br>
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.<br>
# 
# 
# Example 2:
# 
# Input: [1,2,3,4,5,6]<br>
# Output: Node 4 from this list (Serialization: [4,5,6])<br>
# Since the list has two middle nodes with values 3 and 4, we return the second one.<br>
#  
# 
# Note:<br>
# 
# The number of nodes in the given list will be between 1 and 100.<br>

# # Brainstorm
# 
# - check others' ending condition

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        if head.next.next is None:
            return head.next
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        
        if fast.next is None:
            return slow
        return slow.next

