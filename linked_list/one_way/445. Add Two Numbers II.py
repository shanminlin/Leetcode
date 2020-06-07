#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Follow up:<br>
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
# 
# Example:<br>
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)<br>
# Output: 7 -> 8 -> 0 -> 7

# # Brainstorm
# 
# If we reverse the inputs, the problem becomes the same as Add Two Numbers. However, if we don't reverse the string, and computes from the most significant digits, if there is a carry after, we have to find a way to go back to change the numbers, in worst cases, like 99999, we have to change every number in front.
# 
# We can compute the sum from each linked list, then add the two numbers. O(max(m+n)) time. This is possible because Python does not have integer overflow when the number becomes very large.<br>
# We can also store the numbers in linked list to some other data structures. As we iterate the numbers from the most significant digit and want to retrieve the least significant digit first. We can use a stack. We can also use a recursion so we don't need to manipulate the stack explicitly.

# # Solution 1
# ##### Reverse linked lists

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return 
        
        r1 = self.reverse(l1)
        r2 = self.reverse(l2)
        
        carry = 0
        curr1 = r1
        curr2 = r2
        dummy = ListNode(0)
        curr = dummy
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
            
            # Compute digit and carry
            digit = curr_sum % 10
            carry = curr_sum // 10
            
            # Append to new linked list
            curr.next = ListNode(digit)
            curr = curr.next
            
        head = self.reverse(dummy.next)
        return head
    
    def reverse(self, head):
        if not head or head.next is None:
            return head
        
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            
            # Increment pointers
            prev = curr
            curr = next_node
        return prev


# # Solution 2
# ##### Use stack to keep track of numbers and prepend to new list

# In[ ]:


class Solution:
    def addTwoNumbers(self, l1, l2):
        l1_stack = []
        l2_stack = []
        
        curr = l1
        while curr:
            l1_stack.append(curr.val)
            curr = curr.next
        
        curr = l2
        while curr:
            l2_stack.append(curr.val)
            curr = curr.next
            
        carry = 0
        dummy = ListNode(0)
        while l1_stack or l2_stack or carry:
            curr_sum = 0
            if l1_stack:
                curr_sum += l1_stack.pop()
            if l2_stack:
                curr_sum += l2_stack.pop()
            if carry:
                curr_sum += carry
            
            # Compute digit and new carry
            digit = curr_sum % 10
            carry = curr_sum // 10
            
            # Prepend new node
            node = ListNode(digit)
            node.next = dummy.next
            dummy.next = node
        
        return dummy.next

