#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
# 
# The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.
# 
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].
# 
# Some examples:<br>
# 
# "1 + 1" = 2<br>
# " 6-4 / 2 " = 4<br>
# "2*(5+5*2)/3+(6/2+8)" = 21<br>
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12<br>
#  
# 
# Note: Do not use the eval built-in library function.

# In[ ]:


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
                continue
                
            elif char == '+' or char == '-':
                # Handle negative number
                if seen_nums == []:
                    seen_nums.append(0)
                    
                if seen_operators == [] or seen_operators[-1] == '(':
                    seen_operators.append(char)
 
                else:
                    while seen_operators and seen_operators[-1] != '(':
                        b = seen_nums.pop()
                        a = seen_nums.pop()
                        operator = seen_operators.pop()
                        temp = self.evaluate(a, b, operator)
                        seen_nums.append(temp)
                    seen_operators.append(char)
            
            elif char == '*' or char == '/':
                if seen_operators and (seen_operators[-1] == '*' or seen_operators[-1] == '/'):
                    b = seen_nums.pop()
                    a = seen_nums.pop()
                    operator = seen_operators.pop()
                    temp = self.evaluate(a, b, operator)
                    seen_nums.append(temp)
                    
                seen_operators.append(char)
                
            elif char == '(':
                seen_operators.append(char)
                # Handle negative number
                if s[i+1] == '-':
                    seen_nums.append(0)
            
            elif char == ')':
                while seen_operators[-1] != '(':
                    b = seen_nums.pop()
                    a = seen_nums.pop()
                    operator = seen_operators.pop()
                    temp = self.evaluate(a, b, operator)
                    seen_nums.append(temp)
                # Pop '('
                seen_operators.pop()
            
            # else condition is when char is space
            # Increment i
            i += 1
            
        if seen_operators == []:
            return seen_nums[-1]
        else:
            while seen_operators != []:
                b = seen_nums.pop()
                a = seen_nums.pop()
                operator = seen_operators.pop()
                temp = self.evaluate(a, b, operator)
                seen_nums.append(temp)
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

