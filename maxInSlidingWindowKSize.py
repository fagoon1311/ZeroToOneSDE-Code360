from collections import deque
# Problem Statement: Given an array and an integer K. Find the maximum for each and every contiguous subarray of size k.

# Brute Force Approach: We iterate over the array and for each window of size k, we will find the maximum element in that window. 

'''
Time Complexity: O(n*k) where n is the length of the array and k is the size of the window.
Space Complexity: O(1)
'''

def slidingWindowMaximum(nums: list, k: int):
  res = []
  for i in range(len(nums) - k + 1):
      currmax = max(nums[i:i + k])
      res.append(currmax)
  return res


# Optimal Solution: Using Deque

"""
The deque d stores indices of nums, not values.

Indices in d are kept in increasing index order (left → right) and the values at those indices are in strictly decreasing order (so the maximum of the current window is always at d[0]).

For each position i:

Remove indices that are out of the current window (d[0] <= i - k) from the front.

Remove indices from the back while their values nums[d[-1]] <= nums[i] (so new bigger/same value takes precedence).

Append current index i to the back.

If i >= k - 1, record nums[d[0]] as the window maximum.

"""


def slidingWindowMaximum1(nums: list, k: int):
    res = []
    d = deque()

    # Dry run example: nums = [1,3,-1,-3,5,3,6,7], k = 3
    for i in range(len(nums)):

        print("Before popping starts", d)
        # STEP 1: Remove indices out of window
        while d and d[0] <= i - k:
            d.popleft()
        print("After popping out of window", d)
        # STEP 2: Maintain decreasing order (remove smaller elements from back)
        while d and nums[d[-1]] <= nums[i]:
            d.pop()
        print("After popping smaller elements", d)
        # STEP 3: Add current index
        d.append(i)
        print("After adding current index", d)

        # STEP 4: Record result if we have at least k elements processed
        if i >= k - 1:
            res.append(nums[d[0]])

        # -------- DRY RUN COMMENTARY --------
        # i = 0, val = 1 → d = [0] (values [1]), no result yet
        # i = 1, val = 3 → pop 0 (1 <= 3), d = [1] (values [3]), no result yet
        # i = 2, val = -1 → d = [1,2] (values [3,-1]), res = [3]
        # i = 3, val = -3 → d = [1,2,3] (values [3,-1,-3]), res = [3,3]
        # i = 4, val = 5 → pop 1 (out of window), pop 3, pop 2 (all <= 5),
        #                  d = [4] (values [5]), res = [3,3,5]
        # i = 5, val = 3 → d = [4,5] (values [5,3]), res = [3,3,5,5]
        # i = 6, val = 6 → pop 5, pop 4 (<= 6), d = [6] (values [6]), res = [3,3,5,5,6]
        # i = 7, val = 7 → pop 6 (<=7), d = [7] (values [7]), res = [3,3,5,5,6,7]

    return res


# ✅ Example run
print(slidingWindowMaximum1([1,3,-1,-3,5,3,6,7], 3))
# Output: [3, 3, 5, 5, 6, 7]
