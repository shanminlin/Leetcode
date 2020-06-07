#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
# 
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
# 
# Example 1:
# 
# Input: 1->2->3->4->5->NULL<br>
# Output: 1->3->5->2->4->NULL<br>
# 
# 
# Example 2:
# 
# Input: 2->1->3->5->6->4->7->NULL<br>
# Output: 2->3->6->7->1->5->4->NULL<br>
# 
# Note:
# 
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...

# # Brainstorm
# 
# Change the next pointers around.
# - Be careful of while loop ending conditions 
# 

# In[8]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        
        odd_curr = head
        even_head = head.next
        even_curr = even_head

        while odd_curr and odd_curr.next and even_curr.next:
            odd_curr.next = odd_curr.next.next
            odd_curr = odd_curr.next
        
            even_curr.next = even_curr.next.next
            even_curr = even_curr.next
            
        # link the end of curr to even_head
        odd_curr.next = even_head
        
        
        return head

