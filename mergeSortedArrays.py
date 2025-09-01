# Problem: Given two sorted arrays one of size m + n and the other of size n, merge them into a single sorted array. 
# The first array has extra space to hold the second array.

#Solution BRute Force: Merge the two arrays into a new array and then sort the new array. This is O(n log n) time complexity. This is not the best solution.

# Optimal Solution: Use two pointers to merge the two arrays into the first array. This is O(m + n) time complexity.

def mergeSortedArrays(arr1,arr2,m,n):
  # Declare 3 variables to keep track of last index of arr1, arr2 and arr1 + arr2
  i,j , last = m-1 , n-1, m + n - 1
  # Compare the last elements of arr1 and arr2 and place the larger one in the last index of arr1
  while j >= 0:
      if i >= 0 and arr1[i] > arr2[j]:
          arr1[last] = arr1[i]
          i -= 1
      else:
          arr1[last] = arr2[j]
          j -= 1

      last -= 1

  return arr1