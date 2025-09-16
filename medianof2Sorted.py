# Problem statement
# Given two sorted arrays 'a' and 'b' of size 'n' and 'm' respectively.
# Find the median of the two sorted arrays.
# Median is defined as the middle value of a sorted list of numbers. In case the length of list is even, median is the average of the two middle elements.
# The expected time complexity is O(min(logn, logm)), where 'n' and 'm' are the sizes of arrays 'a' and 'b', respectively, and the expected space complexity is O(1).


# Approach1: Since the two arrays are sorted, we can merge them into a single sorted array and then find the median.
"""
Time Complexity: O(n + m)
We dont need to sort the arrays after joining we can use the fact that they are already sorted to save the time.

Space Complexity: O(n + m)
We are using a new array to store the two arrays into one.
"""


def median(a: list, b: list) -> float:
  merged = []
  i = j = 0

  while i < len(a) and j < len(b):
      if a[i] < b[j]:
          merged.append(a[i])
          i += 1
      else:
          merged.append(b[j])
          j += 1

  merged.extend(a[i:])
  merged.extend(b[j:])

  lenm = len(merged)

  if lenm % 2 == 0:
      idx = lenm // 2
      return (merged[idx] + merged[idx - 1])/2

  else:
      return float(merged[lenm//2])


# Approach2: We can use two pointers to traverse the two arrays to eliminate the use of extra space. The two pointers will traverse while keeping track of the count of elements we need to traverse. Once the count is reached we can find the median.

"""
Time Complexity: O(m + n)
Space Complexity: O(1)
"""

def mediann(a: list, b: list) -> float:
    n, m = len(a), len(b)
    total = n + m
    mid1, mid2 = (total - 1) // 2, total // 2   # positions we care about

    i = j = 0
    count = -1
    median1 = median2 = 0

    # simulate merge until we reach mid2
    while i < n or j < m:
        if j >= m or (i < n and a[i] <= b[j]):
            val = a[i]
            i += 1
        else:
            val = b[j]
            j += 1

        count += 1
        if count == mid1:
            median1 = val
        if count == mid2:
            median2 = val
            break  # no need to continue after reaching mid2

    if total % 2 == 0:
        return (median1 + median2) / 2
    else:
        return float(median2)



