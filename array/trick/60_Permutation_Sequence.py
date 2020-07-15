#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# The set [1,2,3,...,n] contains a total of n! unique permutations.<br>
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:<br>
# 
# "123"<br>
# "132"<br>
# "213"<br>
# "231"<br>
# "312"<br>
# "321"<br>
# Given n and k, return the kth permutation sequence.<br>
# 
# Note:
# - Given n will be between 1 and 9 inclusive.
# - Given k will be between 1 and n! inclusive.
# 
# Example 1:<br>
# Input: n = 3, k = 3<br>
# Output: "213"<br>
# 
# Example 2:<br>
# Input: n = 4, k = 9<br>
# Output: "2314"


def get_permutation(n, k):
    nums = [str(i) for i in range(1, n+1)]
    fact = [1] * n
    for i in range(1, n):
        fact[i] = i*fact[i-1]
    k -= 1
    
    permutations = []
    for i in range(n, 0, -1):
        id = k // fact[i-1]
        k %= fact[i-1]
        permutations.append(nums[id])
        nums.pop(id)
    return ''.join(permutations)



