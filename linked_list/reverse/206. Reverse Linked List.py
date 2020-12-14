#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Reverse a singly linked list.
# 
# Example:
# 
# Input: 1->2->3->4->5->NULL<br>
# Output: 5->4->3->2->1->NULL<br>
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# # Brainstorm
# 
# 

# # Solution 1
# ##### Iteration

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        curr = head
        while curr:
            # reverse link
            next_node = curr.next
            curr.next = pre
            
            # next iteration
            pre = curr
            curr = next_node

        return pre




# # Solution 2
# ##### Recursion



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        return self.reverseList_helper(head, None)
        
    def reverseList_helper(self, head, prev):
        
        if head is None:
            return prev
        
        next_node = head.next
        head.next = prev

        return self.reverseList_helper(next_node, head)

