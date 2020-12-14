#!/usr/bin/env python
# coding: utf-8

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# 
# Example:
# 
# Input:<br>
# 1->4->5<br>
# 1->3->4<br>
# 2->6<br>
# Output:<br>
# 1->1->2->3->4->4->5->6

# 
# So we are given k linked lists, which are sorted, and we need to return one sorted linked list.
# 
# Assumptions: - duplicate values?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution priority queue
# time complexity O(Nlogk) where N is the total number of nodes and k is the number of linked lists
# space complexity O(k)
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        queue = []
        for i, node in enumerate(lists):
            if node: # in case the node is empty
                # add val, i to the heapq as 
                # 1. comparing nodes leads to error, we can only compare values
                # 2. if values are the same, we will compare index i. Otherwise we will have error.
                heapq.heappush(queue, (node.val, i, node)) 
        
        # build our final linked list
        head = node = ListNode(0)
        while queue:
            _, i, curr_min = heapq.heappop(queue)
            
            # attach min to the result linked list
            node.next = curr_min
            
            if curr_min.next:
                heapq.heappush(queue, (curr_min.next.val, i, curr_min.next))
                
            node = node.next
                  
        return head.next