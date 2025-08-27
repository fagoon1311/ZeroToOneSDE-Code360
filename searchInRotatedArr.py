# Problem Description: Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]). You are given a target value to search. If found in the array return its index, otherwise return -1. You may assume no duplicate exists in the array. Your algorithm's runtime complexity must be in the order of O(logN).

# Solution:
# Find the mid index.
# If the value(key) being searched for is at the mid index, then return the mid index.
# Compare values at start index, end index, and mid-index:
# If the left subarray is sorted, check if the value(key) to be searched lies in the range:
# If it does, then search space reduces between [start, (mid-1)].
# Otherwise, the search space reduces between [(mid + 1), end]
# If the right subarray is sorted, check if the value(key) to be searched lies in the range:
# If it does, then search space reduces between [(mid + 1), end].
# Otherwise, the search space reduces between [start, (mid -1)]
# Repeat from step-1 until the key is found.
# Return -1 if never found.

def search(arr, target):
  left = 0
  right = len(arr) - 1


  # we use left <= right because we want to include the case where left == right
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return mid

    # if the left subarray is sorted
    elif arr[left] <= arr[mid]:
      # if the target is in the left subarray
      if arr[left] <= target < arr[mid]:
        right = mid - 1
      else:
        left = mid + 1

    # if the right subarray is sorted
    else:
      # if the target is in the right subarray
      if arr[mid] < target <= arr[right]:
        left = mid + 1
      else:
        right = mid - 1
  return -1