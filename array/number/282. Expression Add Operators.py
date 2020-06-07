#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
# 
# Example 1:<br>
# 
# Input: num = "123", target = 6<br>
# Output: ["1+2+3", "1*2*3"] <br>
# 
# Example 2:
# 
# Input: num = "232", target = 8<br>
# Output: ["2*3+2", "2+3*2"]<br>
# 
# Example 3:
# 
# Input: num = "105", target = 5<br>
# Output: ["1*0+5","10-5"]<br>
# 
# Example 4:
# 
# Input: num = "00", target = 0<br>
# Output: ["0+0", "0-0", "0*0"]<br>
# 
# Example 5:
# 
# Input: num = "3456237490", target = 9191<br>
# Output: []
