#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Write a program to find the node at which the intersection of two singly linked lists begins.
# 
# Notes:
# 
# If the two linked lists have no intersection at all, return null.<br>
# The linked lists must retain their original structure after the function returns.<br>
# You may assume there are no cycles anywhere in the entire linked structure.<br>
# Your code should preferably run in O(n) time and use only O(1) memory.

# # Brainstorm
# 
# The challenge is that the number of nodes before intersection for the two lists might be different. So we can't iterate the two lists together from the beginning.

# # Solution 1

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        A_length = self.get_length(headA)
        B_length = self.get_length(headB)
        
        currA = headA
        currB = headB
        
        if A_length > B_length:
            diff = A_length - B_length
            # Iterate A until diff is 0
            while diff > 0:
                currA = currA.next
                diff -= 1

        elif B_length > A_length:
            diff = B_length - A_length
            while diff > 0:
                currB = currB.next
                diff -= 1
        
        # Iterate both list
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        
        return None
    
    def get_length(self, head):
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        return length 

