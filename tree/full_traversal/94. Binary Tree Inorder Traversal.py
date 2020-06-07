#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# <img src='../images/inorder.png'>

# # Solution 1
# ##### DFS

# In[ ]:


def in_order(root):
    seen = []
    helper(root, seen)
    return seen
    
def helper(root, seen):
    if root is None:
        return
    
    helper(root.left, seen)
    seen.append(root.val)
    helper(root.right, seen)


# # Solution 2 
# ##### DFS with explicit stack

# In[ ]:


def inorderTraversal(root):
    if root is None:
        return None

    order = []
    stack = []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        order.append(root.val)
        root = root.right
    return order

