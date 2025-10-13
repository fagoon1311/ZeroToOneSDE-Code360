# You are given an array 'ARR' of integers of length N. Your task is to find the next smaller element for each of the array elements.
# Next Smaller Element for an array element is the first element to the right of that element which has a value strictly smaller than that element.
# If for any array element the next smaller element does not exist, you should print -1 for that array element.
# For Example:
# If the given array is [ 2, 3, 1], we need to return [1, 1, -1]. Because for  2, 1 is the Next Smaller element. For 3, 1 is the Next Smaller element and for 1, there is no next smaller element hence the answer for this element is -1.


# Approach 1: Brute Force
'''
TC: O(n^2)
SC: O(n)
'''
def nextSmallerElement(arr,n):
  res = []

  for i in range(n):
      currMin = arr[i]
      for j in range(i + 1, n):
          if arr[i] > arr[j]:
              currMin = arr[j]
              break

      if currMin != arr[i]:
          res.append(currMin)
      else:
          res.append(-1)

  return res

# Approach 2: Using Stack.

#The idea is to find the Next Smaller Element for each of the N array elements in one iteration of the array by using a stack. Our approach is to traverse the array from right to left and for each array element we will first pop all such elements that are currently at the top of stack and having a value greater than or equal to the current element. Now we will set the Next Smaller Element as the element at the top of the stack if the stack is non-empty otherwise we will set it as -1. Now we will push that element into the stack and move ahead.

'''
Time Complexity: O(n)
Space Complexity: O(n)

'''
def nextSmallerElement1(arr, n):
  stack = []
  res = [-1] * n

  for i in range(n - 1, -1, -1):
      while stack and stack[-1] >= arr[i]:
          stack.pop()

      if stack:
          res[i] = stack[-1]

      stack.append(arr[i])

  return res
