# Problem Description: Given an unsorted array of integers, find the length of longest increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

# Solution: Recursive -> O(2^n) time complexity, O(n) space complexity. 

def recursive(i , p, arr, n):
  if i == n:
    return 0
  notTake = recursive(i + 1, p, arr, n)
  take = 0
  if p == -1 or arr[i] > arr[p]:
    take = 1 + recursive(i + 1, i, arr, n)
  return max(take, notTake)

# Solution: Memoization -> O(n^2) time complexity, O(n^2) space complexity.

def memoization(i , p, arr, n, dp):
  if i == n:
    return 0
  
  # create dp with shift of 1 to avoid negative index 
  # dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
  if dp[i][p] != -1:
    return dp[i][p]
  notTake = memoization(i + 1, p, arr, n, dp)
  take = 0
  if p == -1 or arr[i] > arr[p]:
    take = 1 + memoization(i + 1, i, arr, n, dp)
  dp[i][p] = max(take, notTake)
  return dp[i][p]

# Solution: Tabulation -> O(n^2) time complexity, O(n^2) space complexity. 
def tabulation(arr, n):
  dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
  for i in range(n - 1, -1, -1):
    for p in range(i - 1, -2, -1):
      notTake = dp[i + 1][p + 1]
      take = 0
      if p == -1 or arr[i] > arr[p]:
        take = 1 + dp[i + 1][i + 1]
      dp[i][p + 1] = max(take, notTake)
  return dp[0][0]

# Solution: Space Optimization -> O(n^2) time complexity, O(n) space complexity.
# we only need the current row and the next row to calculate the current row. so we can optimize the space complexity to O(n).
def spaceOptimization(arr, n) :

  nextRow = [0 for _ in range(n+1)]
  curr = [0 for _ in range(n + 1)]
  
  for i in range(n - 1, -1, -1):
      for p in range(i - 1, -2, -1):
          notTake = 0 + nextRow[p + 1]
          take = 0
          if p == -1 or arr[i] > arr[p]:
              take = 1 + nextRow[i + 1]
  
          curr[p + 1] = max(take, notTake)
  
      nextRow = curr

  return nextRow[0]

# Solution: Tabulation -> O(n^2) time complexity, O(n) space complexity. We use only single array to store previous indexes max length of subsequence.

def tabulation2(arr, n): 
  dp = [1 for _ in range(n)]
  for i in range(n):
    for j in range(i):
      if arr[i] > arr[j]:
        dp[i] = max(dp[i], dp[j] + 1)
  return max(dp)


# Solution: Binary Search -> O(n log n) time complexity, O(n) space complexity.

# This is the basic intuition of the algorithm. If we make a new LIS array at every junction, it will take up a lot of space. Now the question arises, do we need to store all these extra LIS arrays in a data structure to keep track of all the LIS formed as we traverse the array?

#The answer is No, We can maintain a single array (say temp) and rewrite this temp array again in order to find the length of the LIS. We are concerned about the length of the LIS rather than the LIS itself.

# We can use binary search to find the position of the current element in the temp array. If the current element is greater than the last element of the temp array, we append the current element to the temp array. Otherwise, we replace the first element.

def binarySearch(arr, n):
  left, right = 0, len(arr)
  while left < right:
    mid = (left + right)//2
    if arr[mid] == n:
      return mid

    elif arr[mid] < n:
      left = mid + 1

    else:
      right = mid

  return left
    

def findLongestIncreasingSubsequence(arr, n):
  res = [arr[0]]
  for i in range(1, n):
    if arr[i] > res[-1]:
      res.append(arr[i])
    else:
      idx = binarySearch(res, arr[i])
      res[idx] = arr[i]
  return len(res)
    