#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# There are a total of n courses you have to take, labeled from 0 to n-1. Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]<br>
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?<br>
# 
# Example 1:<br>
# Input: 2, [[1,0]]<br> 
# Output: true<br>
# Explanation: 
# There are a total of 2 courses to take.<br>
# To take course 1 you should have finished course 0. So it is possible.<br>
# 
# Example 2:<br>
# Input: 2, [[1,0],[0,1]]<br>
# Output: false<br>
# Explanation:<br>
# There are a total of 2 courses to take.<br>
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
# 
# Note:
# - The input prerequisites is a graph represented by a list of edges, not adjacency matrices. 
# - You may assume that there are no duplicate edges in the input prerequisites.

# # Brainstorm
# 
# It is possible for a course to have several prerequisites. In that case, you have to finish all prerequisites to take that course.
# 
# 
# We have n numbers of courses, and their relationships. As their relationship is nonlinear and has direction, a directed graph seems suitable to model their relationship. 
# 
# What are the characteristics of the graph if we can't finish all courses? Think about connectivity, directions, cycles which are main properties of a graph that affects its traversal.
# 
# - What if there is a node that is not connected? just take it, no effect
# - What if there are two way direction, meaning a cycle? aha, then we can't finish the courses in the cycle.
# 
# 
# Use a dictionary {course: prerequisites} or {prerequisite: courses}? 
# 
# Traverse: start from a node that has no reprequisites. From that node, if we can traverse all courses, then it is possible to final all courses.
# 
# Need a indegree list, a dictionary to represent relationships, a queue to process, and num_courses to keep track no. of courses taken.

# # Solution 

# In[ ]:


from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):

    graph = defaultdict(list)
    indegree = [0] * numCourses

    # Collect adjacencies for prereq->list(courses).
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        
        # Count number of requisites for each course
        indegree[course] += 1

    queue = deque()

    for course in range(numCourses):
        # For course with no prerequisites, we can take them.
        if indegree[course] == 0:
            queue.append(course)

    visited = 0
    while queue:
        # Take course with no prerequisites.
        prerequisite = queue.popleft()
        visited += 1
        
        # What courses can be taken after taking the prerequisits?
        
        for course in graph[prerequisite]:
            indegree[course] -= 1

            # If there is no more prerequisites, take next course.
            if indegree[course] == 0:
                queue.append(course)

    return visited == numCourses


# Space： O(N), we have the graph, indegree list and a queue
# Time: O(N^2), we traverse the prerequisite list, the numcourses, and the queue; for each item in queue, we traverse the graph.

# Build adjacency list from edge list

# In[4]:


from collections import defaultdict
graph = defaultdict(list)
for child, parent in edge_list:
    graph[parent].append(child)


# In[8]:


graph = {}
for child, parent in edge_list:
    if parent not in graph:
        graph[parent] = []
    graph[parent].append(child)


# In[ ]:




