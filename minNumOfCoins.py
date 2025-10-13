# Given an infinite supply of Indian currency i.e. [1, 2, 5, 10, 20, 50, 100, 500, 1000] valued coins and an amount 'N'.Find the minimum coins needed to make the sum equal to 'N'. You have to return the list containing the value of coins required in decreasing order.

# Solution: The main idea behind this approach is to use a greedy algorithm. We start by taking the largest coin that is less than or equal to the remaining amount. We keep doing this until the remaining amount becomes 0.

# Why greedy works? Until we have a canonical coin system, greedy works. If we had a custom non canonical coin system, then greedy would not work. And solution would be to use dynamic programming with either memoization or tabulation.

'''
Time Complexity: O(n) in the worst case

Space Complexity: O(n) in the worst case (number of coins stored in res)
'''

from typing import List

def MinimumCoins(n: int) -> List[int]:
    # write your code here
    coins = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

    res = []

    for coin in coins:
        while n >= coin:
            n -= coin
            res.append(coin)

    return res
