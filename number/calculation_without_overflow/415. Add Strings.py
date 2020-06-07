#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.<br>
# Both num1 and num2 contains only digits 0-9.<br>
# Both num1 and num2 does not contain any leading zero.<br>
# You must not use any built-in BigInteger library or convert the inputs to integer directly.<br>

# # Solution 1

# In[2]:


class Solution:
    def addStrings(self, num1, num2):
        
        # From least significant digit,
        # convert character to digit 
        # sum digit and carry
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        curr_sum = 0
        power = 0
        total_sum = 0
        while i >= 0 or j >= 0 or carry:
            curr_sum = 0
            
            if i >= 0:
                curr_sum += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                curr_sum += ord(num2[j]) - ord('0')
                j -= 1
            if carry:
                curr_sum += carry
                
            carry = curr_sum // 10
            digit = curr_sum % 10
            total_sum = digit * (10**power) + total_sum
            base += 1
        return str(total_sum)


# # Solution 2

# In[ ]:


class Solution:
    def addStrings(self, num1, num2):
        
        # From least significant digit,
        # convert character to digit 
        # sum digit and carry
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        curr_sum = 0
        total_sum = ''
        while i >= 0 or j >= 0 or carry:
            curr_sum = 0
            
            if i >= 0:
                curr_sum += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                curr_sum += ord(num2[j]) - ord('0')
                j -= 1
            if carry:
                curr_sum += carry
                
            carry = curr_sum // 10
            digit = curr_sum % 10
            
            total_sum += str(digit)
            
        return total_sum[::-1]


# As string concatenation creates a new string every time, we can use a list.

# In[ ]:


class Solution:
    def addStrings(self, num1, num2):
        
        # From least significant digit,
        # convert character to digit 
        # sum digit and carry
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        curr_sum = 0
        total_sum = []
        while i >= 0 or j >= 0 or carry:
            curr_sum = 0
            
            if i >= 0:
                curr_sum += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                curr_sum += ord(num2[j]) - ord('0')
                j -= 1
            if carry:
                curr_sum += carry
                
            carry = curr_sum // 10
            digit = curr_sum % 10
            
            total_sum.append()
        
        total_sum = ''.join(total_sum)    
        return total_sum[::-1]

