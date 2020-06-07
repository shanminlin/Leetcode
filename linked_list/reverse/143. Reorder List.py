#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# You may not modify the values in the list's nodes, only nodes itself may be changed.
# 
# Example 1:
# 
# Given 1->2->3->4, reorder it to 1->4->2->3.
# 
# Example 2:
# 
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# # Brainstorm
# 
# The ending condition for even and odd length is very troublesome.

# # Solution

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
    
        """
        
        # Edge
        if not head or not head.next or not head.next.next:
            return head
        
        
        # Find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        # Now slow is at the middle
        # reverse list from slow to end
        
        prev = None
        curr = slow
        next_node = curr.next
        while curr:
            curr.next = prev
            
            # increment three pointers
            prev = curr
            curr = next_node
            if curr:
                next_node = curr.next
                
        # now prev is the reverse head
        
        front_curr = head
        back_curr = prev
        front_next = front_curr.next
        back_next = back_curr.next
        
        while back_next:
            
            front_curr.next = back_curr
            back_curr.next = front_next
            
            front_curr = front_next
            back_curr = back_next
            
            front_next = front_next.next
            back_next = back_next.next
            
        return head
        

