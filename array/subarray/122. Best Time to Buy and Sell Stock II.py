#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Say you have an array prices for which the ith element is the price of a given stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
# 
# Example 1:<br>
# 
# Input: [7,1,5,3,6,4]<br>
# Output: 7<br>
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Example 2:<br>
# 
# Input: [1,2,3,4,5]<br>
# Output: 4<br>
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# 
# Example 3:<br>
# 
# Input: [7,6,4,3,1]<br>
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#  
# 
# Constraints:
# 
# 1 <= prices.length <= 3 * 10 ^ 4
# 0 <= prices[i] <= 10 ^ 4

# # Solution

# In[ ]:


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = -1 # in case no sell until the end of the array
        profits = 0
        i = 0
        while i < len(prices):
            # Buy first, then sell
            while i + 1 < len(prices) and prices[i+1] < prices[i]:
                buy = i + 1
                i += 1
            
            while i + 1 < len(prices) and prices[i+1] >= prices[i]:
                sell = i + 1
                i += 1
            
        
            profits += prices[sell] - prices[buy]
            i += 1
            buy = i
            sell = -1
        
        return profits

