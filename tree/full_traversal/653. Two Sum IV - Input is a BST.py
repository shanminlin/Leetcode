#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
# 
# <img src='../images/twosum.png'>

# # Brainstorm
# 
# 

# Approach 1: use a set and depth first search

# In[ ]:


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def findTarget(root, k):
    seen = set()
    return find(root, k, seen)

def find(root, k, seen):
    if root is None:
        return False
    
    if (k - root.val) in seen:
        return True
    
    seen.add(root.val)
    return find(root.left, k, seen) or find(root.right, k, seen)


# Approach 2: breath first search

# In[ ]:


from collections import deque

def findTarget(root, k):
    seen = set()
    queue = deque()
    queue.append(root)

    while queue:
        if queue[0] is not None:
            node = queue.popleft()
            if (k - node.val) in seen:
                return True
            seen.add(node.val)
            queue.append(node.right)
            queue.append(node.left)
        else:
            queue.popleft()

    return False


# Approach 3: BST

# In[ ]:


def findTarget(root, k):
    nums = []
    self.inorder(root, nums)
    l = 0
    r = len(nums) - 1
    while l < r:
        two_sum = nums[l] + nums[r]
        if two_sum == k:
            return True
        elif two_sum > k:
            r -= 1
        else:
            l += 1
    return False

def inorder(self, root, nums):
    if root is None:
        return nums

    self.inorder(root.left, nums)
    nums.append(root.val)
    self.inorder(root.right, nums)

