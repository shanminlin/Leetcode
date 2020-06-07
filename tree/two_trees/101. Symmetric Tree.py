#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# <img src='./images/symmetric_tree.png'>

# # Brainstorm
# 
# What are the characteristics of a symmetric tree?
# - If level order traversal, each level is a palindrome.

# # Solution 1
# recursion

# In[ ]:


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_symmetric(root):
    if root is None:
        return True
    return is_mirror(root.left, root.right)

def is_mirror(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False

    if node1.val == node2.val:
        return is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)


# Time complexity : O(n)O(n). Because we traverse the entire input tree once, the total run time is O(n)O(n), where nn is the total number of nodes in the tree.
# 
# Space complexity : The number of recursive calls is bound by the height of the tree. In the worst case, the tree is a linear symmetric tree, which is a tree where every left child has only a left child, until leaf; and right child has only right child until leaf. That is a right angle tree someone referred above. Height will be n/2, hence O(n) complexity

# same approach using recursion stack

# In[ ]:


def is_symmetric(root):
    if root is None:
        return True

    stack = [(root.left, root.right)]
    while stack:
        node1, node2 = stack.pop()
        if node1 is None and node2 is None:
            continue
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False

        stack.append((node1.left, node2.right))
        stack.append((node1.right, node2.left))
    return True


# - each time we just need to store one level nodes.
# - in a full binary tree, bottom level has O(n/2) nodes.

# Approach 2: BFS
# - use a queue to store the nodes
# - check whether the first node pair has equal values
# - if so, go on to append subsequent pair
# 

# In[ ]:


from collections import deque
def is_symmetric(root):
    if root is None:
        return True

    queue = deque([(root.left, root.right)])

    while queue:
        node1, node2 = queue.popleft()
        if node1 is None and node2 is None:
            continue
        if node1 is None or node2 is None:
            return False

        if node1.val != node2.val:
            return False

        queue.append((node1.left, node2.right))
        queue.append((node1.right, node2.left))
    return True

