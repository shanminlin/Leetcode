#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Implement the following operations of a queue using stacks.<br>
# 
# push(x) -- Push element x to the back of queue.<br>
# pop() -- Removes the element from in front of queue.<br>
# peek() -- Get the front element.<br>
# empty() -- Return whether the queue is empty.<br>
# 
# Example:
# 
# MyQueue queue = new MyQueue();<br>
# 
# queue.push(1);<br>
# queue.push(2);<br>
# queue.peek();  // returns 1<br>
# queue.pop();   // returns 1<br>
# queue.empty(); // returns false<br>
# 
# Notes:
# 
# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.<br>
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.<br>
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

# # Brainstorm
# 
# Use two stacks
# - push O(1)
# - pop O(N) amortize O(1)
# 
# 

# # Solution

# In[ ]:


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack = []
        self.outstack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.instack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.outstack.pop()
        
            
    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.outstack == []:
            length = len(self.instack)
            
            # Transfer all items in instack to outstack
            for _ in range(length):
                item = self.instack.pop()
                self.outstack.append(item)
            return self.outstack[-1]
        # If outstack stll got elements
        return self.outstack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # Elements split in instack and outstack
        # so both stacks need to be empty
        return self.instack == [] and self.outstack == []

