#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Implement the following operations of a stack using queues.<br>
# 
# push(x) -- Push element x onto stack.<br>
# pop() -- Removes the element on top of the stack.<br>
# top() -- Get the top element.<br>
# empty() -- Return whether the stack is empty.<br>
# 
# Example:
# 
# MyStack stack = new MyStack();<br>
# 
# stack.push(1);<br>
# stack.push(2);<br>
# stack.top();   // returns 2<br>
# stack.pop();   // returns 2<br>
# stack.empty(); // returns false<br>
# 
# Notes:
# 
# You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.<br>
# Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.<br>
# You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
# 

# # Brainstorm
# 
# - push O(N) to reverse the queue
# - pop O(1)

# In[ ]:


from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # Store its original length
        length = len(self.stack)
        
        self.stack.append(x)
        for _ in range(length):
            item = self.stack.popleft()
            self.stack.append(item)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.stack) == 0

