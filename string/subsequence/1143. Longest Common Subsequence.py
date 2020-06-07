#!/usr/bin/env python
# coding: utf-8

# 1143. Longest Common Subsequence

# 1. Recursion

# In[3]:


def lcs(text1, text2):
    return helper(len(text1)-1, len(text2)-1, text1, text2)

def helper(i, j, text1, text2):
    if i < 0 or j < 0:
        return 0
    
    elif text1[i] == text2[j]:
        return 1 + helper(i-1, j-1, text1, text2)
    
    else:
        return max(helper(i-1, j, text1, text2), helper(i, j-1, text1, text2))


# In[4]:


lcs("abcde", "ace")


# In[5]:


lcs("abc","def")


# 2. Memoization
# We can see that there are many subproblems that are solved again and again. So this problem has Overlapping Substructure property and recomputation of same subproblems can be avoided by either using Memoization or Tabulation.

# In[25]:


def lcs(text1, text2):

    end_i = len(text1) - 1
    end_j = len(text2) - 1
    dp = [[-1 for _ in range(len(text1))] for _ in range(len(text2))]


    return helper(text1, text2, end_i, end_j, dp)


# In[26]:


def helper(text1, text2, i, j, dp):

    if i == 0 or j == 0:
        return 0

    elif dp[i][j] != -1:
        return dp[i][j]

    elif text1[i] == text2[j]:
         1 + helper(text1, text2, i-1, j-1, dp)

    else:
        dp[i][j] = max(helper(text1, text2, i-1, j, dp), helper(text1, text2, i, j-1, dp))
        
    return dp[-1][-1]


# In[27]:


lcs("abcde", "ace")


# In[ ]:




