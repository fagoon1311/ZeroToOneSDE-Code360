#Problem Description: Given an integer array nums, find the contiguous subarray (including empty subArr) which has the largest sum and return its sum.

#Solution: Brute Force -> O(n^3) time complexity, O(1) space complexity. For each pair of indices, calculate the sum of the subarray between them.

def bruteForce(arr, n):
  maxSum = 0
  for i in range(n):
    for j in range(i, n):
      sum = 0
      for k in range(i, j + 1):
        sum += arr[k]
      maxSum = max(maxSum, sum)
  return maxSum

# Solution: Brute Force with Cumulative Sum -> O(n^2) time complexity, O(n) space complexity. For each pair of indices, calculate the sum of the subarray between them using the cumulative sum array.

def bruteForceCumulativeSum(arr, n):
  maxSum = 0
  for i in range(n):
    curr = 0
    for j in range(i, n):
      curr += arr[j]
      maxSum = max(maxSum, curr)
  return maxSum


# Solution: Kadane's Algorithm -> O(n) time complexity, O(1) space complexity. For each element, calculate the maximum sum of the subarray ending at that element. If this value is negative, then the maximum sum of the sub array ending at that element is the element itself. Otherwise, the maximum sum of the subarray ending at that element is the sum of the element and the maximum sum of the subarray ending at the previous element.

def kadane(arr, n):
  maxSum = -float('inf')
  curr = 0
  for i in range(n):
    curr += arr[i]
    maxSum = max(maxSum, curr)
    if curr < 0:
      curr = 0
  return maxSum

