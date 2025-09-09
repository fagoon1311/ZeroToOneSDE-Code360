# Problem: Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

#Solution1: Brute Force: The brute force approach is to traverse each element in the array ('NUM' = ‘ARR[i]’) and then keep finding ('NUM' + 1) in the array until we don't find the next consecutive element in the array. Keep a track of the current length of the sequence. If the current length of the consecutive subsequence is greater than the longest length of consecutive subsequence then update it.

'''
    Time Complexity: O(N^3)
    Space Complexity: O(1) 

    Where N is the length of array.
'''

# To check whether currNum is present in array or not.
def arrayItContains(currNum, n, arr):
    for i in range(n):
        if (arr[i] == currNum):
            return True

    return False


def lengthOfLongestConsecutiveSequence(arr, n): 
    # To store length of longest consecutive sequence.
    mx = 0

    for i in range(n):
        count = 1

        # Making arr[i] as first element of sequence.
        currNum = arr[i]

        while arrayItContains(currNum + 1, n, arr):
            # Setting currNum to be next consecutive element by increament.
            currNum += 1
            count += 1

        # Update maximum length of consecutive sequence if any.
        mx = max(mx, count)

    return mx


# Solution2: Sorting: The idea is to sort the array and then find the longest consecutive sequence. The time complexity of this approach is O(NlogN) due to sorting.

'''
    Time Complexity: O(N*logn(N))
    Space Complexity: O(1)

    Where N is the length of array.
'''

def lengthOfLongestConsecutiveSequence1(arr,n):

   # Sort the given array in ascending order.
   arr.sort()

   # To store length of longest consecutive sequence.
   mx = 0

   # To store the length of current consecutive Sequence.
   count = 0

   for i in range(n):

        # Check if previous value is consecutive to the current value.
        if (i > 0 and  (arr[i] == arr[i - 1] + 1)):

            count += 1

        # Skip if the current value is equals to the previous value.
        elif (i > 0 and  arr[i] == arr[i - 1]):
                continue

        # Reseting count for next upcoming consecutive sequence.
        else:
            count = 1

        mx = max(mx,count)

   return mx



# Solution3: Using a set: The idea is to use a set to store the elements of the array. If a preceeding element is not present in the set, then it is the starting point of a new sequence. We keep track of the length of the current sequence and update the maximum length of the sequence if the current sequence is longer than the maximum sequence.

def lengthOfLongestConsecutiveSequence2(arr, n):
  # Write your code here.
  numset = set(arr)
  longest = 0

  for n in numset:
      if n - 1 not in numset:
          length = 1
          while n + length in numset:
              length += 1
          longest = max(length, longest)

  return longest
  pass
