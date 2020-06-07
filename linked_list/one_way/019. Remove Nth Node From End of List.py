#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a linked list, remove the n-th node from the end of list and return its head.
# 
# Example:<br>
# 
# Given linked list: 1->2->3->4->5, and n = 2.<br>
# 
# After removing the second node from the end, the linked list becomes 1->2->3->5.<br>
# 
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?

# # Brainstorm
# 
# We can first get the length of the linked list length.
# - when we reach length - 2 node, the next node need to be skipped
# - so curr.next = curr.next.next
# 
# Can we do it in one pass? Think of multiple pointers.
# 
# 
# Edge cases
# - linked list with only one node: use "dummy" node to simplify such cases.
# 

# # Solution 1
# ##### Calculate length

# In[ ]:


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        if head is None:
            return 
        
        if n == 0:
            return head
        
        # Get length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        # from beginning
        k = length - n 
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        count = 1
        while count <= k:
            curr = curr.next
            count += 1
            
        curr.next = curr.next.next
        
        return dummy.next


# # Solution 2
# ##### Two pointers
