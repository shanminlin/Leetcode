#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .<br>
# 
# Example 1:
# 
# Input: "1 + 1"<br>
# Output: 2<br>
# 
# Example 2:
# 
# Input: " 2-1 + 2 "<br>
# Output: 3<br>
# 
# Example 3:
# 
# Input: "(1+(4+5+2)-3)+(6+8)"<br>
# Output: 23<br>
# 
# Note:
# You may assume that the given expression is always valid.<br>
# Do not use the eval built-in library function.

# # Problem
# 
# The problem has several complications for finding a patten:
# 
# 

# In[8]:


class Solution:
    def calculate(self, s):
        # Edge cases
        if not s:
            return 0
        
        seen_nums = []
        seen_operators = []
        num = 0
        i = 0
        # Use while loop instead of for loop 
        # as we will skip i in the first if condition
        # for computing numbers
        while i < len(s):
            char = s[i]
            if char.isdigit():
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                seen_nums.append(num)
                num = 0
                continue
                
            elif char == '+' or char == '-':
                if not seen_operators or seen_operators[-1] == '(':
                    seen_operators.append(char)
                else:
                    b = seen_nums.pop()
                    a = seen_nums.pop()
                    operator = seen_operators.pop()
                    temp_num = self.evaluate(a, b, operator)
                    seen_nums.append(temp_num)
                    seen_operators.append(char)
            
            elif char == '(':
                seen_operators.append(char)
            
            elif char == ')':
                while seen_operators[-1] != '(':
                    b = seen_nums.pop()
                    a = seen_nums.pop()
                    operator = seen_operators.pop()
                    temp_num = self.evaluate(a, b, operator)
                    seen_nums.append(temp_num)
                # Pop '('
                seen_operators.pop()
                
            i += 1
        
        if seen_operators == []:
            return seen_nums[-1]
        else:
            b = seen_nums.pop()
            a = seen_nums.pop()
            operator = seen_operators.pop()
            num = self.evaluate(a, b, operator)
            return num
        
    def evaluate(self, a, b, operator):
        if operator == '+':
            return a + b
        if operator == '-':
            return a - b

