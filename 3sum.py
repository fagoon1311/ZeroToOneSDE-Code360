# Problem => You are given an array/list ARR consisting of N integers. Your task is to find all the distinct triplets present in the array which adds up to a given number K.

# BruteForce Solution: We can use three nested loops to find all the triplets that add up to K. The outer loop will iterate over the array, the second loop will iterate over the array from the next element of the outer loop, and the third loop will iterate over the array from the next element of the second loop. If the sum of the three elements is equal to K, we add the triplet to the result list. We also need to check if the triplet is already present in the result list to avoid duplicates. The time complexity of this solution is O(n^3) and the space complexity is O(1).


def findTriplets(arr, n, K):
    res = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == K:
                    if [arr[i], arr[j], arr[k]] not in res:
                        res.append([arr[i], arr[j], arr[k]])


# Optimized Solution: We can use two pointers to find the triplets that add up to K. We sort the array first. Then we iterate over the array with a loop. For each element, we use two pointers to find the other two elements. The left pointer starts from the next element of the current element and the right pointer starts from the last element of the array. If the sum of the three elements is equal to K, we add the triplet to the result list. If the sum is less than K, we move the left pointer to the right. If the sum is greater than K, we move the right pointer to the left. The time complexity of this solution is O(n^2) and the space complexity is O(1 + n) = O(n).

def findTriplets2(arr, n, k):
    arr.sort()
    res = []
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        l, r = i + 1, n - 1
        while l < r:
            if arr[i] + arr[l] + arr[r] == k:
                res.append([arr[i], arr[l], arr[r]])
                l += 1
                while l < r and arr[l] == arr[l - 1]:
                    l += 1
            elif arr[i] + arr[l] + arr[r] < k:
                l += 1
            else:
                r -= 1