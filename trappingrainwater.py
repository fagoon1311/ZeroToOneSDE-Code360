# Problem Description: Given an array of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# Solution: Brute Force -> O(n^2) time complexity, O(1) space complexity. For each bar, find the maximum height of the bar to the left and right. The water trapped on top of the bar is the minimum of the two heights minus the height of the bar.

def bruteForce(arr, height):
  n = len(arr)
  ans = 0
  for i in range(n):
    leftMax = 0
    rightMax = 0
    for j in range(i):
      leftMax = max(leftMax, arr[j])
    for j in range(i + 1, n):
      rightMax = max(rightMax, arr[j])

    ans += max(0, min(leftMax, rightMax) - arr[i])
  return ans

# Solution: Precompute the left and right maximum heights -> O(n) time complexity, O(n) space complexity. For each bar, the water trapped on top of the bar is the minimum of the left and right maximum heights minus the height of the bar. If this value is negative, then no water is trapped on top of the bar.

def precompute(arr, height):
  n = len(arr)
  leftMax = [0] * n
  rightMax = [0] * n
  ans = 0
  leftMax[0] = arr[0]
  rightMax[n - 1] = arr[n - 1]
  for i in range(1, n):
    leftMax[i] = max(leftMax[i - 1], arr[i])

  for i in range(n - 2, -1, -1):
    rightMax[i] = max(rightMax[i + 1], arr[i])

  for i in range(n):
    ans += max(0, min(leftMax[i], rightMax[i]) - arr[i])

  return ans

# Solution: Two Pointers -> O(n) time complexity, O(1) space complexity. Use two pointers to keep track of the left and right maximum heights. If the left maximum height is less than the right maximum height, then the water trapped on top of the bar is the left maximum height minus the height of the bar. Otherwise, the water trapped on top of the bar is the right maximum height minus the height of the bar. If this value is negative, then no water is trapped.

def twoPointers(arr, height):
  n = len(arr)
  ans = 0
  leftMax = 0
  rightMax = 0
  left = 0
  right = n - 1
  while left < right:
    if arr[left] < arr[right]:
      leftMax = max(leftMax, arr[left])
      ans += max(0, leftMax - arr[left])
      left += 1
    else:
      rightMax = max(rightMax, arr[right])
      ans += max(0, rightMax - arr[right])
      right -= 1
  return ans