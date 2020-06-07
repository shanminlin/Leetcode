#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.
# 
# For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.
# 
# Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.
# 
# Example 1:<br>
# 
# Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1<br>
# Output: 11<br>
# Explanation:<br>
# Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.<br>
#  
# 
# Note:
# 
# One employee has at most one direct leader and may have several subordinates.<br>
# The maximum number of employees won't exceed 2000.

# # Brainstorm
# 
# BFS
# - usually we use a queue to process the nodes for BFS. In this case, the order of node processing does not matter, we can use a stack (python list) to process it as well.
# 
# - The id, importance and subordinates information are stored as an Employee class. The subordinates only contain ids. So we have to search the employees list to get the corresponding importance for each id. N(1 + eN). To reduce the time complexity, we use a hash table to store employee class and employee id. 

# # Solution 1
# ##### BFS

# In[ ]:


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        start = None
        for employee in employees:
            if employee.id == id:
                start = employee
                
        queue = deque([start])
        visited = set()
        total_importance = 0
        
        while queue:
            employee = queue.popleft()
            visited.add(employee)
            total_importance += employee.importance
            
            for subordinate in employee.subordinates:
                if subordinate not in visited:
                    for employee in employees:
                        if subordinate == employee.id:
                            queue.append(employee)
                    
        return total_importance


# In[ ]:


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        start = None
        employee_dict = {}
        for employee in employees:
            if employee.id == id:
                start = employee
            
            if employee.id not in employee_dict:
                employee_dict[employee.id] = None
            employee_dict[employee.id] = employee
                
        queue = deque([start])
        visited = set()
        total_importance = 0
        
        while queue:
            employee = queue.pop()
            visited.add(employee)
            total_importance += employee.importance
            
            for subordinate_id in employee.subordinates:
                if subordinate_id not in visited:
                    queue.append(employee_dict[subordinate_id])
 
        return total_importance


# # Solution 2
# ##### DFS

# In[6]:


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        employee_dict = {}
        for employee in employees:
            if employee.id not in employee_dict:
                employee_dict[employee.id] = None
            employee_dict[employee.id] = employee
            
        employee = employee_dict[id]
        visited = set()
        return self.dfs(employee_dict, employee, visited)
        
        
    def dfs(self, employee_dict, employee, visited):
        
        visited.add(employee.id)
        
        total_importance = employee.importance
        for subordinate_id in employee.subordinates:
            if subordinate_id not in visited:
                total_importance += self.dfs(employee_dict, employee_dict[subordinate_id], visited)
        
        return total_importance

