# Problem: Your task is to find the ‘K’ most frequent elements in ‘ARR’. Return the elements in any order.

# Brute Force Solution: We can use a dictionary to count the frequency of each element in the array. Then we can sort the dictionary by the frequency of the elements. Finally, we can return the first ‘K’ elements in the sorted dictionary.

'''
Time Complexity: 
couting the frequency of each element in the array takes O(n) time.
sorting the dictionary by the frequency of the elements takes O(n log n) time.
returning the first ‘K’ elements in the sorted dictionary takes O(k) time.
So the total time complexity is O(n log n).

If we use selection sort or bubble sort, the time complexity will be O(n^2).

Space Complexity:
We are using a dictionary to count the frequency of each element in the array. So the space complexity is O(n).


'''
from typing import List
def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
  count = {}

  for num in arr:
      if num in count:
          count[num] += 1
      else:
          count[num] = 1



  sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)
  # python's sorted function uses timsort algorithm which has a time complexity of O(n log n)
  # if you use selection sort or bubble sort, the time complexity will be O(n^2)
  

  top_k = [item[0] for item in sorted_items[:k]]

  return top_k



# Optimized SOlution: We can utilize bucket sort. We can create a list of lists, where the index of the list is the frequency of the element. We can iterate through the array and count the frequency of each element. Then we can iterate through the list of lists and return the first ‘K’ elements that we encounter.

def KMostFrequentk(n: int, k: int, arr: List[int]) -> List[int]:
    count = {}

    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1



    bucket = [[] for _ in range(n + 1)]

    for num, freq in count.items():
        bucket[freq].append(num)

    res = []
    for freq in range(n, 0 , -1):
        for num in bucket[freq]:
            res.append(num)
            if len(res) == k:
                return res

  
