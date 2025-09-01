import heapq
# Problem: Given an array of integers, find the kth largest element in the array.

# Solution: Sort the array in descending order and return the kth element. Time complexity is O(n log n). Space complexity is O(1).

def kthLargestNumber(arr, k):
  arr.sort(reverse=True)
  return arr[k-1]


# Optimal Solution: Use a min heap to keep track of the k largest elements. Time complexity is O(n log k). Space complexity is O(k).
def kthLargest(arr, size, k):
  
  pq = []
  for i in range(size):
      if i < k:
          heapq.heappush(pq, arr[i])
      else:
          val = pq[0]
          if val < arr[i]:
              heapq.heappop(pq)
              heapq.heappush(pq, arr[i])
  return pq[0]
  