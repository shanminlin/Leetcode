#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
# 
# You have the following 3 operations permitted on a word:
# 
# Insert a character<br>
# Delete a character<br>
# Replace a character<br>
# 
# Example 1:<br>
# Input: word1 = "horse", word2 = "ros"<br>
# Output: 3<br>
# Explanation: <br>
# horse -> rorse (replace 'h' with 'r')<br>
# rorse -> rose (remove 'r')<br>
# rose -> ros (remove 'e')<br>
# 
# Example 2:<br>
# Input: word1 = "intention", word2 = "execution"<br>
# Output: 5<br>
# Explanation:<br>
# intention -> inention (remove 't')<br>
# inention -> enention (replace 'i' with 'e')<br>
# enention -> exention (replace 'n' with 'x')<br>
# exention -> exection (replace 'n' with 'c')<br>
# exection -> execution (insert 'u')<br>

# # Brainstorm
# 
# 

# In[ ]:


# check if they are one edit or zero edits away
def oneAway(string1, string2):
    
    if (len(string1) - len(string2) > 1) or (len(string2) - len(string1) > 1):
        return False
    
    elif len(string1) - len(string2) == 1:
        count = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                string2 = string2[:i] + "F" + string2[i:]
                count += 1
                
    elif len(string2) - len(string1) == 1:
        count = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                string2 = string2[:i] + "F" + string2[i:]
                count += 1
                
    else:
        count = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                count += 1
    
    if count == 1:
        return True
    else:
        return False        

