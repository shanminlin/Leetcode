#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# Input: 1->2
# Output: false
# Example 2:
# 
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# # Solution 1
# ##### Store first half in an array

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        
        # find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        
        # go to the middle
        mid = length // 2
        num = 0
        curr = head
        first_half = []
        while num < mid:
            num += 1
            first_half.append(curr.val)
            curr = curr.next
            
        # compare 
        if length % 2 == 1:
            curr = curr.next
        
        i = mid - 1
        while curr:
            if curr.val != first_half[i]:
                return False
            curr = curr.next
            i -= 1
            
        return True


# # Solution 2
# ##### Pointer and reverse 

# In[18]:


def ispalindrome(head):
    # get length
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    print(length)
        
    mid = length // 2
    print(mid)
    
    mid_node = head
    for _ in range(mid):
        mid_node = mid_node.next
    
    # Reverse from mid_node to last node
    prev_node = None
    curr = mid_node
    while curr:
        next_node = curr.next
        curr.next = prev_node
        prev_node = curr
        curr = next_node
        
    # Now prev_node is the last node
    # compare
    for _ in range(mid):
        if head.value != prev_node.value:
            return False
        head = head.next
        prev_node = prev_node.next
    
    return True


# In[2]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# In[27]:


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)


# In[23]:


ispalindrome(head)


# ## Improve finding middle node

# In[24]:


def ispalindrome(head):

    mid_node = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        mid_node = mid_node.next
    
    # Reverse from mid_node to last node
    prev_node = None
    curr = mid_node
    while curr:
        next_node = curr.next
        curr.next = prev_node
        prev_node = curr
        curr = next_node
        
    # Now prev_node is the last node
    # compare fist and second half
    while prev_node and head:
        if head.value != prev_node.value:
            return False
        head = head.next
        prev_node = prev_node.next
    
    return True


# In[28]:


ispalindrome(head)


# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        
        mid_node = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            mid_node = mid_node.next

        # Reverse from mid_node to last node
        prev_node = None
        curr = mid_node
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        # Now prev_node is the last node
        # compare fist and second half
        while prev_node and head:
            if head.val != prev_node.val:
                return False
            head = head.next
            prev_node = prev_node.next

        return True
        

