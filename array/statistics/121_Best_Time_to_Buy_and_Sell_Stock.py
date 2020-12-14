# -*- coding: utf-8 -*-
"""
Problem
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

# Solution: time O(N), space O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == [] or prices is None:
            return 0
        
        diff = 0
        min_price = prices[0]
        max_price = prices[0]
        for i in range(1, len(prices)):
            
            # if current price is lower than current min,
            # start a new trend
            if prices[i] < min_price:
                min_price = prices[i]
                max_price = prices[i]
                
            # if current price is higher than current max,
            # continue the present trend
            elif prices[i] > max_price:
                max_price = prices[i]
                diff = max(diff, max_price - min_price)
                
            # if current price is in between min and max price,
            # no use
            else:
                continue
        
        return diff