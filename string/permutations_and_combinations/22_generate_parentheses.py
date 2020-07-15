#!/usr/bin/env python
# coding: utf-8

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

["((()))", "(()())", "(())()", "()(())", "()()()"]
"""
class Solution:
    def generateParenthesis(self, n):
        if n <= 0:
            return []
        
        temp_str = ''
        result= []
        nopen = n
        nclose = n
        self.helper(temp_str, nopen, nclose, result)
        return result
    
    def helper(self, temp_str, nopen, nclose, result):
        if nopen == 0 and nclose == 0:
            result.append(temp_str)
            return
        
        if nopen == nclose:
            self.helper(temp_str+'(', nopen-1, nclose, result)
            
        elif nclose > nopen and nopen > 0:
            self.helper(temp_str+'(', nopen-1, nclose, result)
            self.helper(temp_str+')', nopen, nclose-1, result)
        
        else: # nopen == 0:
            self.helper(temp_str+')', nopen, nclose-1, result)