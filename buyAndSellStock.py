# Problem - You are given an array/list 'prices' where the elements of the array represent the prices of the stock as they were yesterday and indices of the array represent minutes. Your task is to find and return the maximum profit you can make by buying and selling the stock. You can buy and sell the stock only once.


# Solution1 - Brute Force Approach - We can use two nested loops to find the maximum profit. The outer loop will iterate over the array and the inner loop will iterate over the array from the next element of the outer loop to the end of the array. We will calculate the profit for each pair.

'''
TC = O(n^2)
SC = O(1)
'''

def maximumProfit(prices):
    maxProfit = 0
    n = len(prices)

    for i in range(n - 1):
        buy = prices[i]
        curMaxProfit = 0

        for j in range(i + 1, n):
            curMaxProfit = max(curMaxProfit, (prices[j] - buy))

        maxProfit = max(maxProfit, curMaxProfit)

    return maxProfit

# Optimised Solution - We can use single loop to find the maximum profit. We will maintain two variables, 'minPrice' and 'maxProfit'. We will iterate over the array and update the 'minPrice' if the current price is less than the 'minPrice'. We will update the 'maxProfit' if the difference between the current price and the 'minPrice' is greater than the 'maxProfit'.


'''
TC = O(n)
SC = O(1)
'''
def maximumProfit1(prices):

  mini = prices[0]
  profit = 0

  for i in range(1, len(prices)):
      cost = prices[i] - mini
      profit = max(cost, profit)
      mini = min(prices[i], mini)

  return profit
