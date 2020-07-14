#!/usr/bin/env python
# coding: utf-8

# # Problem 
# 
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.<br>
# 
# Note:
# - All numbers will be positive integers.
# - The solution set must not contain duplicate combinations.
# 
# Example 1:<br>
# Input: k = 3, n = 7<br>
# Output: [[1,2,4]]<br>
# 
# Example 2:<br>
# Input: k = 3, n = 9<br>
# Output: [[1,2,6], [1,3,5], [2,3,4]]

# In[ ]:


def combinationSum3(self, k: int, n: int) -> List[List[int]]:
       result = []
       nums = [i  for i in range(1,10)]
       def backtrack(nums,index,n,k,path):
           if n < 0:
               return
           if k == 0 and n == 0:
               result.append(path)
               return
           for i in range(index,len(nums)):
               if nums[i] > n:
                   continue
               backtrack(nums,i+1,n-nums[i],k-1,path+[nums[i]])
       backtrack(nums,0,n,k,[])
       return result

