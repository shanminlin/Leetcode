#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a linked list, rotate the list to the right by k places, where k is non-negative.
# 
# Example 1:
# 
# Input: 1->2->3->4->5->NULL, k = 2<br>
# Output: 4->5->1->2->3->NULL
# 
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL<br>
# rotate 2 steps to the right: 4->5->1->2->3->NULL<br>
# 
# Example 2:
# 
# Input: 0->1->2->NULL, k = 4<br>
# Output: 2->0->1->NULL<br>
# 
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL<br>
# rotate 2 steps to the right: 1->2->0->NULL<br>
# rotate 3 steps to the right: 0->1->2->NULL<br>
# rotate 4 steps to the right: 2->0->1->NULL

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Edge cases
        if not head or not head.next or k == 0:
            return head
        
        # Get the lenght of the lis
        
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        # Edge cases
        #if k == length:
            #return head
        
        #elif k > length:
            #while k > length:
                #k -= length
        k %= length
        if k == 0:
            return head
        
        rotate_times = length - k
        
        curr = head
        while rotate_times > 1:
            curr = curr.next
            rotate_times -= 1
        
        new_head = curr.next
        curr.next = None
        
        curr = new_head
        while curr.next:
            curr = curr.next
            
        curr.next = head
        
        return new_head

