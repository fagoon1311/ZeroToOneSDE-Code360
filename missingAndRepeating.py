# Problem: Given an array of size N it contains all integers from 1 to N. One integer is missing and one integer is repeating. Find the missing and repeating integer.

# Brute Force Solution: We find the missing element by using 2 loops. We iterate over the array and compare to find repeating element. To find missing element we can use the formula : sum of first N natural numbers - sum of array elements + repeating element.


'''
TC - O(N^2)
SC - O(1)
'''
def missingAndRepeating(arr, n):
  # Write your code here
  repeat = missing = arr[0]
  for i in range(n):
      for j in range(i + 1, n):
          if arr[i] == arr[j]:
              repeat = arr[i]

  arrsum = (n * (n + 1))//2
  missing = arrsum - (sum(arr) - repeat)
  return missing, repeat

# Approach 2: We can sort the array first and then find the repeating element by comparing adjacent elements. To find missing element we can use the formula : sum of first N natural numbers - sum of array elements + repeating element.

'''
TC - O(NlogN))
We are sorting the array which takes O(N * log(N)) time. We are also traversing the array which requires O(N) time. Thus, the final time complexity is O(N * log(N) + N) = O(N * log(N)).

SC - O(1)
'''
def missingAndRepeating2(arr, n):
  # Write your code here
  arr.sort()
  repeat = missing = arr[0]
  for i in range(n - 1):
      if arr[i] == arr[i + 1]:
          repeat = arr[i]
  arrsum = (n * (n + 1))//2
  missing = arrsum - (sum(arr) - repeat)
  return missing, repeat


# Solution 3: We can create a count array of size n. We iterate over the array and increment the count of the element in the count array. We iterate over the count array and find the missing and repeating element.

'''
TC - O(N + N) = O(N))
SC - O(N)
'''

def missingAndRepeating3(arr, n):
    # Write your code here
    count = [0] * n
    repeat = missing = arr[0]

    for i in range(n):
        count[arr[i] - 1] += 1

    for i in range(n):
        if count[i] == 0:
            missing = i + 1
        if count[i] > 1:
            repeat = i + 1

    return missing, repeat


# Optimal : The idea is to traverse the array and mark the visited elements.While traversing the array, we will use the absolute value of every element as an index and make the value at this index as negative to mark it visited. For example, for element 3, we will make the value at index 2 as negative ( since the array is 0-indexed ). For any element in the array, if the element at the index {element - 1} is already marked negative, then this is the repeating element. To find the missing number, we will traverse the array again and look for a positive value. The index at which we find the positive value is our missing number because that index is not present in the array as an element.  



# For Example: Consider the array Arr = { 1, 5, 2, 2, 3 }. 

# Now we will traverse the array and mark the visited numbers as follows: 

# At index 0, we encounter 1. To mark this element as visited, Arr[1 - 1] = - Arr[1 - 1].
# Current array Arr: {-1, 5, 2, 2, 3}. 

# At index 1, we encounter 5. To mark this element as visited, Arr[5 - 1] = - Arr[5 - 1].
# Current array Arr: {-1, 5, 2, 2, -3}. 

# At index 2, we encounter 2. To mark this element as visited, Arr[2 - 1] = - Arr[2 - 1].
# Current array Arr: {-1, -5, 2, 2, -3}. 

# At index 3, again we encounter 2.
# Here, the element at index 1 (2 - 1), is already negative. It means we have already visited it. Thus, we have found our repeating number ‘R’ which is 2. 

# Current array Arr: {-1, -5, 2, 2, -3}. 

# At index 4, we encounter 3. To mark this element as visited, Arr[3 - 1] = - Arr[3 - 1].
# Current array Arr: {-1, -5, -2, 2, -3}. 

# To find the missing number ‘M’, we will again traverse the array.
# We will find that the element at index 3 is the only positive element. It means that the missing number is 3 + 1 = 4.
# So, our missing number ‘M’ is 4 and the repeating number ‘R’ is 2. 

"""
Time Complexity
O(N), where N is the number of elements in the given array.
We are traversing the given array twice. Thus, the final time complexity is O(N + N) = O(N). 

Space Complexity
O(1)

We are not using any extra data structure. Only constant additional space is required.
"""
def missingAndRepeating4(arr, n):
  repeating = -1
  missing = -1

  # Step 1: Find the repeating number
  for i in range(n):
      idx = abs(arr[i]) - 1
      if arr[idx] < 0:
          repeating = abs(arr[i])
      else:
          arr[idx] = -arr[idx]

  # Step 2: Find the missing number
  for i in range(n):
      if arr[i] > 0:
          missing = i + 1
          break

  return (missing, repeating)



