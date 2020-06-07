#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Example:<br>
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)<br>
# Output: 7 -> 0 -> 8<br>
# Explanation: 342 + 465 = 807.

# # Brainstorm
# 
# - Time O(max(m, n), space O(max(m, n))

# In[29]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Edge case
        if not l1 and not l2:
            return 
        
        carry = 0
        curr1 = l1
        curr2 = l2
        head = None
        while curr1 or curr2 or carry:
            curr_sum = 0

            if curr1:
                curr_sum += curr1.val
                curr1 = curr1.next
            if curr2:
                curr_sum += curr2.val
                curr2 = curr2.next
            if carry:
                curr_sum += carry
                
            carry = curr_sum // 10
            curr_sum = curr_sum % 10
            
            # Append sum to combined list
            if not head:
                head = ListNode(curr_sum)
                curr = head
            else:         
                curr.next = ListNode(curr_sum)
                curr = curr.next
 
        return head


# Use a dummy node to reduce edge case checking:

# In[ ]:


class Solution:
    def addTwoNumbers(self, l1, l2):
        # Edge case
        if not l1 and not l2:
            return 
        
        carry = 0
        curr1 = l1
        curr2 = l2
        dummy = ListNode(0)
        curr = dummy
        while curr1 or curr2 or carry:
            curr_sum = 0
            
            # Check node valid or not separately
            # If check together, too many cases
            # E.g if curr1 and curr2 and carry, etc..
            if curr1:
                curr_sum += curr1.val
                curr1 = curr1.next
            if curr2:
                curr_sum += curr2.val
                curr2 = curr2.next
            if carry:
                curr_sum += carry
                
            carry = curr_sum // 10
            curr_sum = curr_sum % 10
            
            # Append sum to combined list
            curr.next = ListNode(curr_sum)
            curr = curr.next
 
        return dummy.next

