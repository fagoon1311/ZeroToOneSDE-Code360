# Problem - Find The length of maximum conescutive ones in a binary array that can be created by replacing at  most k zeroes.

# Solution 1 - Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def longestSubSeg_bruteforce(arr, n, k):
  res = 0

  for i in range(n):
      zero = 0
      for j in range(i, n):
          if arr[j] == 0:
              zero += 1

          # If flips exceed k, break
          if zero > k:
              break

          res = max(res, j - i + 1)

  return res


# Optimized Solution: Sliiding Window 
'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
def longestSubSeg(arr, n, k):
  l = 0
  res = 0
  zero = 0


  for r in range(n):
      if arr[r] == 0:
          zero += 1

      while zero > k:
          if arr[l] == 0:
              zero -= 1
          l += 1

      res = max(res, r - l + 1)

  return res
