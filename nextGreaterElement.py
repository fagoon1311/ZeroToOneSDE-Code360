# Problem: Given an array of integers, find the next greater element for each element in the array. The next greater element for an element x is the first greater element that is to the right of x in the array. If there is no such element, output -1 for this element.

# Solution: Use a stack to keep track of the elements that we have not found the next greater element for. We iterate through the array from right to left. If the current element is greater than the top of the stack, we pop the stack until the top of the stack is greater than the current element. Then we push the current element onto the stack. If the current element is less than or equal to the top of the stack, we push the current element onto the stack.

def nextGreaterElement(arr):
  stack = [arr[-1]]
  res = [-1]
  for i in range(len(arr) - 2, -1, -1):
    if arr[i] < stack[-1]:
      res.append(stack[-1])
    else:
      while stack and arr[i] >= stack[-1]:
        stack.pop()
        
        if not stack:
          res.append(-1)
          break

        if stack[-1] > arr[i]:
          res.append(stack[-1])
          break
    stack.append(arr[i])
  return res[::-1]

print(nextGreaterElement([5,4,3,2,1]))
