#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
# 
# For example,<br>
# [2,3,4], the median is 3<br>
# 
# [2,3], the median is (2 + 3) / 2 = 2.5<br>
# 
# Design a data structure that supports the following two operations:
# 
# - void addNum(int num) - Add a integer number from the data stream to the data structure.
# - double findMedian() - Return the median of all elements so far.
#  
# 
# Example:<br>
# addNum(1)<br>
# addNum(2)<br>
# findMedian() -> 1.5<br>
# addNum(3) <br>
# findMedian() -> 2<br>
#  
# 
# Follow up:
# - If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# - If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

# Approach 1: Brute force
# - store the element in a resizable container. Everytime you need to output the median, sort the container and output the median

# In[ ]:


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.container = []

    def addNum(self, num: int) -> None:
        self.container.append(num)

    def findMedian(self) -> float:
        self.container.sort()
        
        if len(self.container) % 2 == 0:
            median_index_left = int(len(self.container) / 2 - 1)
            median_index_right = int(len(self.container) / 2)
            median = (self.container[median_index_left] + self.container[median_index_right]) / 2
        else:
            median_index = int(len(self.container) // 2)
            median = self.container[median_index]
        return median
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# Time complexity: O(nlogn)+O(1)≃O(nlogn).
# 
# Adding a number takes amortized O(1)O(1) time for a container with an efficient resizing scheme.
# Finding the median is primarily dependent on the sorting that takes place. This takes O(n\log n)O(nlogn) time for a standard comparative sort.
# Space complexity: O(n)O(n) linear space to hold input in a container. No extra space other than that needed (since sorting can usually be done in-place).

# Approach 2: insertion sort using binary search

# In[ ]:


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        
    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
            return 
        l = 0
        r = len(self.nums)-1
        while l < r:
            m = (l+r)//2
            if self.nums[m] == num:
                self.nums.insert(m,num)
                return 
            elif self.nums[m] < num:
                l = m+1
            else:
                r = m-1      
        if self.nums[l] < num:
            self.nums.insert(l+1,num)
        else:
            self.nums.insert(l,num)

    def findMedian(self) -> float:
        mid = (0 + len(self.nums)-1 )//2
        if (len(self.nums)-1) & 1:
            return (self.nums[mid] + self.nums[mid+1])/2
        else:
            return self.nums[mid]


# Approach 3: heap
# - Time complexity: O(logn)

# In[ ]:


import heapq

class MedianFinder:
    def __init__(self):
        self.small = [] # max queue
        self.large = [] # min queue

    def addNum(self, num):
        if len(self.small) == 0:
            # max heap is the negative of min heap
            heapq.heappush(self.small, -num)
            return
        
        if num <= -self.small[0]:
            # push to small part
            heapq.heappush(self.small, -num)
        else:
            # push to large part
            heapq.heappush(self.large, num)
            
        # adjust small and large balance
        if len(self.small) - len(self.large) == 2:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.small) - len(self.large) == -2:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.0
        
        elif len(self.small) > len(self.large):
            return -float(self.small[0])
        else:
            return float(self.large[0])


# Approach 4: BST

# Approach 5: binary tree
