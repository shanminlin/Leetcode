#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given two strings text1 and text2, return the length of their longest common subsequence.
# 
# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
# 
#  
# 
# If there is no common subsequence, return 0.
# 
#  
# 
# Example 1:<br>
# 
# Input: text1 = "abcde", text2 = "ace" <br>
# Output: 3<br>
# Explanation: The longest common subsequence is "ace" and its length is 3.<br>
# 
# Example 2:
# 
# Input: text1 = "abc", text2 = "abc"<br>
# Output: 3<br>
# Explanation: The longest common subsequence is "abc" and its length is 3.<br>
# 
# Example 3:
# 
# Input: text1 = "abc", text2 = "def"<br>
# Output: 0<br>
# Explanation: There is no such common subsequence, so the result is 0.<br>
#  
# 
# Constraints:
# 
# 1 <= text1.length <= 1000<br>
# 1 <= text2.length <= 1000<br>
# The input strings consist of lowercase English characters only.

# # Brainstorm
# 
# 

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


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        end_i = len(text1) - 1
        end_j = len(text2) - 1
        dp = [[-1 for _ in range(len(text1))] for _ in range(len(text2))]
        
        def helper(text1, text2, i, j, dp):

            
            if i < 0 or j < 0:
                return 0
            
            elif dp[i][j] != -1:
                return dp[i][j]
            
            elif text1[i] == text2[j]:
                dp[i][j] = 1 + helper(text1, text2, i-1, j-1, dp)
                return dp[i][j]
            
            else:
                dp[i][j] = max(helper(text1, text2, i-1, j, dp), helper(text1, text2, i, j-1, dp))
                return dp[i][j]
            
        return helper(text1, text2, end_i, end_j, dp)
            

