# Problem Statement: Given an array of integers. Find the Inversion Count in the array. An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].

# Solution1: Brute Force - We traverse the array and for each element, we traverse the array again and count the number of elements greater than the current element. We start from back so that i < j is satisfied without having to check.

'''
Time Complexity - O(n ^ 2)
SC - O(1)
'''

def getInversions(arr, n):
  res = 0
  for j in range(len(arr) - 1, -1, -1):
      for i in range(j - 1, -1, -1):
          if arr[i] > arr[j]:
              res += 1
  return res



# Solution2: Merge  Sort - We use merge sort to count the number of inversions. We count the number of inversions while merging two halves of the array. We use a temporary array to store the merged array. We use two pointers to traverse the two halves of the array. We compare the elements at the two pointers and if the element in the left half is greater than the element in the right half, we count the number of elements in the right half that are greater than the element in the left half.

def merge(arr, mid, low, high):
    temp = []
    left = low 
    right = mid + 1
    cnt = 0

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1

        else:
            temp.append(arr[right])
            cnt += mid - left + 1
            right += 1




    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1


    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return cnt


def mergeSort(arr, low , high):
    cnt = 0
    if low >= high:
        return cnt
    mid = (low + high)//2
    cnt += mergeSort(arr, low, mid)    # left half
    cnt += mergeSort(arr, mid + 1, high)  # right half
    cnt += merge(arr, mid, low, high)  # merging sorted halves
    return cnt

def getInversions2(arr, n):
    return mergeSort(arr, 0, n - 1) 


