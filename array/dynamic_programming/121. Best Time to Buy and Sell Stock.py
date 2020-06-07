#!/usr/bin/env python
# coding: utf-8

# 121. Best Time to Buy and Sell Stock

# In[ ]:


def maxProfit(self, prices: List[int]) -> int:
    if prices is None or prices == []:
        return 0
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit

