#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a set of distinct integers, nums, return all possible subsets (the power set).<br>
# 
# Note: The solution set must not contain duplicate subsets.<br>
# 
# Example:<br>
# Input: nums = [1,2,3]<br>
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# # Brainstorm
# 
# This question seems easy but it is not.
# 

# append() or **+=** will modify the same copy. 

# In[32]:


nums = [1, 2, 3]


# In[35]:


all_combinations = []

for i in range(len(nums)):
    subset = [nums[i]]
    all_combinations.append(subset)
    for j in range(i+1, len(nums)):
        subset.append(nums[j])
        all_combinations.append(subset)
        


# In[36]:


all_combinations


# In[39]:


nums = [1, 2, 3]
all_combinations = []
for num in nums:
    all_combinations.append([num])
print(all_combinations)


# In[52]:


nums = [1, 2, 3, 4]
all_combinations = []


for i in range(len(nums)):
    subset = [nums[i]]
    all_combinations.append(subset[:])
    
    
    for j in range(i+1, len(nums)):
        subset = [nums[i]]
        subset.append(nums[j])
        all_combinations.append(subset[:])
        
        for k in range(j+1, len(nums)):   
            subset.append(nums[k])
            all_combinations.append(subset[:])          

print(all_combinations)
print(len(all_combinations))


# - copy vs modify mutable object 
#     - list.append() adds a reference to the list, not a copy. 
# - keep track inside the for loop is not trivial. How about saving outside the loop and update?

# In[86]:


def subsets(nums):
    all_subsets = [[]]
    
    for num in nums:
        for i in range(len(all_subsets)): # use length to record the length of all_subsets before appending
            all_subsets.append(all_subsets[i]+[num]) # cancatenation to create new list
    return all_subsets


# In[104]:


def subsets_test(nums):
    all_subsets = [[]]
    
    for num in nums:
        for i in range(len(all_subsets)):
            
            all_subsets[i].append(num)
            all_subsets.append(all_subsets[i])
    return all_subsets


# In[105]:


subsets_test([1, 2, 3])


# In[100]:


def subsets(nums):
    all_subsets = [[]]
    if not nums:
        return all_subsets
    for num in nums:
        for subset in all_subsets[:]:
            temp = subset + [num]
            all_subsets.append(temp) # this results in infinite loop.
    return all_subsets


# In[ ]:





# # Solution 1: bottom up 

# Solution 2: top down dynamic programming

# In[72]:


def subsets(nums):
    subsets = []
    dfs(subsets, [], nums, 0)
    return subsets

def dfs(subsets, templist, nums, start):
    subsets.append(templist)
    for i in range(start, len(nums)):
        dfs(subsets, templist+[nums[i]], nums, i+1)


# In[73]:


nums = [1, 2, 3]


# In[74]:


subsets(nums)


# Solution 3: backtrack

# In[69]:


def find_subsets(nums):
    subsets = []
    backtrack(subsets, 0, [])
    return subsets

def backtrack(subsets, start, templist):
    subsets.append(templist[:])
    for i in range(start, len(nums)):
        templist.append(nums[i])
        backtrack(subsets, i+1, templist)
        templist.pop()


# In[70]:


nums = [1, 2, 3]


# In[71]:


find_subsets(nums)

