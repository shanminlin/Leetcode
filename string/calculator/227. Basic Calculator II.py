#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
# 
# Example 1:<br>
# 
# Input: "3+2*2"<br>
# Output: 7<br>
# 
# Example 2:<br>
# 
# Input: " 3/2 "<br>
# Output: 1<br>
# 
# Example 3:<br>
# 
# Input: " 3+5 / 2 "<br>
# Output: 5<br>
# 
# Note:
# 
# You may assume that the given expression is always valid.<br>
# Do not use the eval built-in library function.

# In[7]:


class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        seen_nums = []
        seen_operators = []
        num = 0
        i = 0
        
        while i < len(s):
            char = s[i]
            if char.isdigit():
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                seen_nums.append(num)
                num = 0
                # Contunue because at the bottom we increment i
                # for other cases
                continue
                
            elif char == '+' or char == '-':
                if not seen_operators:
                    seen_operators.append(char)
                else:
                    while seen_operators != []:
                        b = seen_nums.pop()
                        a = seen_nums.pop()
                        operator = seen_operators.pop()
                        temp_num = self.evaluate(a, b, operator)
                        seen_nums.append(temp_num)
                    seen_operators.append(char)
                    
            elif char == '*' or char == '/':
                if not seen_operators:
                    seen_operators.append(char)
                else:
                    if seen_operators[-1] == '+' or seen_operators[-1] == '-':
                        seen_operators.append(char)
                    else:
                        b = seen_nums.pop()
                        a = seen_nums.pop()
                        operator = seen_operators.pop()
                        temp_num = self.evaluate(a, b, operator)
                        seen_nums.append(temp_num)
                        seen_operators.append(char)
            
            i += 1
            
        if seen_operators == []:
            return seen_nums[-1]
        else:
            while seen_operators != []:
                b = seen_nums.pop()
                a = seen_nums.pop()
                operator = seen_operators.pop()
                temp_num = self.evaluate(a, b, operator)
                seen_nums.append(temp_num)
            return seen_nums[-1]
        
    def evaluate(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        else:
            return a // b

