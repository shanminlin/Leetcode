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

# In[29]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        prev = head
        curr = prev.next
        next_node = curr.next
        head.next = None
        
        while curr:
            
            curr.next = prev
            
            # next iteration
            prev = curr
            curr = next_node
            if curr: # Be careful of the end here
                next_node = curr.next
        
        return prev


# In[19]:


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None:
            return head
        
        prev = None
        
        while head:
            
            next_node = head.next
            # reverse link
            head.next = prev
            prev = head
            head = next_node
            
        return prev


# In[32]:


s = Solution()


# In[33]:


new_head = s.reverseList1(head)


# In[28]:


head.next


# In[ ]:





# # Solution 2
# ##### Recursion

# In[ ]:


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        return self.reverseList_helper(head, None)
        
    def reverseList_helper(self, head, prev):
        
        if head is None:
            return prev
        
        next_node = head.next
        head.next = prev

        return self.reverseList_helper(next_node, head)

