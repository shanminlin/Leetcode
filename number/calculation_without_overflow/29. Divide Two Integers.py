#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
# 
# Return the quotient after dividing dividend by divisor.
# 
# The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
# 
# Example 1:<br>
# 
# Input: dividend = 10, divisor = 3<br>
# Output: 3<br>
# Explanation: 10/3 = truncate(3.33333..) = 3.<br>
# 
# Example 2:<br>
# 
# Input: dividend = 7, divisor = -3<br>
# Output: -2<br>
# Explanation: 7/-3 = truncate(-2.33333..) = -2.<br>
# 
# Note:
# 
# Both dividend and divisor will be 32-bit signed integers.<br>
# The divisor will never be 0.<br>
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
