#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the two partitions.
# 
# Example:
# 
# Input: head = 1->4->3->2->5->2, x = 3<br>
# Output: 1->2->2->4->3->5

# # Brainstorm
# 
# Be careful of cycles
# 
# - Time O(N)
# - Space O(1), we are just adjusting the links, not using extra space.
# 

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        if not head or not head.next:
            return head
        
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        less_curr = less_dummy
        greater_curr = greater_dummy
        
        curr = head
        while curr:
            if curr.val >= x:
                greater_curr.next = curr
                greater_curr = greater_curr.next
            else:
                less_curr.next = curr
                less_curr = less_curr.next
                
            curr = curr.next   
        
        less_curr.next = greater_dummy.next
        greater_curr.next = None
        return less_dummy.next

