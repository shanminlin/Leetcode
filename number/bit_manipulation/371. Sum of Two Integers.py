#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
# 
# Example 1:<br>
# 
# Input: a = 1, b = 2<br>
# Output: 3<br>
# 
# Example 2:<br>
# 
# Input: a = -2, b = 3<br>
# Output: 1

# In[1]:


0x7FFFFFFF


# In[2]:


0x80000000


# In[3]:


0xFFFFFFFF


# In[ ]:


# 32 bits integer max
      MAX = 0x7FFFFFFF
      # 32 bits interger min
      MIN = 0x80000000
      # mask to get last 32 bits
      mask = 0xFFFFFFFF

