#Problem Statement - You are given an array “arr'' of integers. Your task is to find the contiguous subarray within the array which has the largest product of its elements. You have to report this maximum product.
# An array c is a subarray of array d if c can be obtained from d by deletion of several elements from the beginning and several elements from the end.

# Solution1: Brute Force
'''
Time Complexity: O(n^2)
Space Complexity: O(1)

'''
def maximumProduct(arr, n):
  res = -float('inf')
  for i in range(n):
      curr = arr[i]
      for j in range(i + 1, n):
          curr *= arr[j]
          res = max(curr, res)
      res = max(res, arr[i])
  return res


# SOlution2: We use two variables to store product sum from left and right. At each index we calculate cumm prod. If the current element is 0, we reset the cumm prod to 1. We also keep track of the max product.

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''

def maximumProduct2(arr, n):
    res = -float('inf')
    leftProd = 1
    rightProd = 1
    for i in range(n):
        leftProd *= arr[i]
        rightProd *= arr[n - i - 1]

        res = max(res, leftProd, rightProd)

        if leftProd == 0:
            leftProd = 1
        if rightProd == 0:
            rightProd = 1

    return res
