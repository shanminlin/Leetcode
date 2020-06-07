#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# 
# Return the linked list sorted as well.
# 
# Example 1:
# 
# Input: 1->2->3->3->4->4->5<br>
# Output: 1->2->5<br>
# 
# 
# Example 2:
# 
# Input: 1->1->1->2->3<br>
# Output: 2->3

# # Brainstorm

# In[ ]:





# # Solution

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return 
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr and curr.next:
            
            if curr.val == curr.next.val:
            
                while curr.next and curr.val == curr.next.val:
                    curr.next = curr.next.next
            
                curr = curr.next
                prev.next = curr
                
                
            else:
                curr = curr.next              
                prev = prev.next
        
        return dummy.next

