#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.<br>
# 
# Example 1:<br>
# Input: 2, [[1,0]] <br>
# Output: [0,1]<br>
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
#              course 0. So the correct course order is [0,1] .<br>
#              
# Example 2:<br>
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]<br>
# Output: [0,1,2,3] or [0,2,1,3]<br>
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .<br>
# 
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

# # Solution 1
# ##### Topological sort

# In[6]:


from collections import deque 
def findOrder(numCourses, prerequisites):
        if numCourses <= 0:
            return []
        
        graph = {}
        indegree = [0] * numCourses
        
        for child, parent in prerequisites:
            if parent not in graph:
                graph[parent] = []
            graph[parent].append(child)
            
            indegree[child] += 1
            
        queue = deque()
        for course, num_prerequisites in enumerate(indegree):
            if num_prerequisites == 0:
                queue.append(course)
                
        if not queue:
            return []
        
        schedule = []
        while queue:
            parent = queue.popleft()
            schedule.append(parent)

            if parent in graph: # if using defaultdict, no need to check.
                for child in graph[parent]:
                    indegree[child] -= 1

                    if indegree[child] == 0:
                        queue.append(child)

        if len(schedule) < numCourses:
            return []
        else:
            return schedule   


# In[7]:


numCourses = 2
prerequisites = [[1, 0]]

findOrder(numCourses, prerequisites)


# # Solution 2
# ##### DFS using visited array (some people use graph coloring)
