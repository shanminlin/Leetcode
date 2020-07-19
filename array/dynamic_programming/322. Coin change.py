#!/usr/bin/env python
# coding: utf-8

"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

# 1. Greedy 
# - This generates wrong result for cases like [4, 6], amount=14
def coinChange(coins, amount):

    coins.sort()

    i = len(coins) - 1
    max_coin = coins[i]
    coin_count = 0

    while amount > 0:       
        while max_coin > amount and i > 0:
            i -= 1
            max_coin = coins[i]

        amount -= max_coin
        coin_count += 1

    if amount == 0:
        return coin_count
    else:
        return -1


# 2. Dynamic programming (bottom up)

def coinChange(self, coins: List[int], amount: int) -> int:

    coins.sort()

    aux = [0] + [float('inf') for _ in range(1, amount + 1)] 

    for coin in coins:
        for subamount in range(coin, amount+1):
            aux[subamount] = min(1 + aux[subamount-coin], aux[subamount])

    return aux[-1] if aux[-1] != float('inf') else -1

