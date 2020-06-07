#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# <img src='./images/construct_tree.png'>

# # Brainstorm
# 
# 

# - Say we have 2 arrays, PRE and IN.
# - Preorder traversing implies that PRE[0] is the root node.
# - Then we can find this PRE[0] in IN, say it's IN[5].
# - Now we know that IN[5] is root, so we know that IN[0] - IN[4] is on the left side, IN[6] to the end is on the right side.
# - Recursively doing this on subarrays
