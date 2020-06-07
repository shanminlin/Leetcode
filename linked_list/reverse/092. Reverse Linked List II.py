#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Reverse a linked list from position m to n. Do it in one-pass.<br>
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4<br>
# Output: 1->4->3->2->5->NULL

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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if not head or not head.next or m == n:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        slow_steps = 1
        while slow_steps < m:
            slow = slow.next
            slow_steps += 1
            
         
        prev = slow
        reverse_head = slow.next
        curr = reverse_head
        next_node = curr.next
        reverse_steps = 1
        while reverse_steps <= n - m + 1:
            curr.next = prev
            
            prev = curr
            curr = next_node
            if curr:
                next_node = curr.next
            
            reverse_steps += 1
            
        
        # connect all
        slow.next = prev
        reverse_head.next = curr
        
   
        return dummy.next

