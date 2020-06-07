#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# 
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# Note: The length of path between two nodes is represented by the number of edges between them.

# # Brainstorm
# 
# Finding the recursive relation is not trivial.
# 
# - how to keep track of the maximium diameter so far?
# 

# # Solution

# In[ ]:


# how to remove the global variable?

def diameterOfBinaryTree(root):
    ans = 0


    def depth(node):
        if not node: 
            return 0
        L = depth(node.left)
        R = depth(node.right)

        ans = max(ans, L+R)
        return max(L, R) + 1

    depth(root)
    return ans

