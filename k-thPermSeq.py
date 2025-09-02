import math
# Solution: Generate all permutations of the string and sort them. Then return the k-th permutation. 
# Recursion takes O(n!) time complexity. Sorting takes O(n log n) time complexity. So the overall time complexity is O(n! * n log n).
# This is not the best solution. We can do better.

def generatePerms(ind, s, ans):
  if ind == len(s):
      ds = []
      for i in range(len(s)):
          ds.append(s[i])
      ans.append(ds)
      return 

  for i in range(ind, len(s)):
      s[ind], s[i] = s[i], s[ind]
      generatePerms(ind + 1, s, ans)
      s[ind], s[i] = s[i], s[ind]



def getKthPermutation(n, k):
  number = [i for i in range(1, n + 1)]
  print(number)
  ans = []
  generatePerms(0, number, ans)
  ans.sort()
  print(ans)
  return ans[k - 1]
  

print(getKthPermutation(3, 6))


# Solution2: We can use the fact that the number of permutations of n elements is n!. We can use this to our advantage to find the k-th permutation in O(n) time complexity. We can use the fact that the number of permutations of n elements starting with a particular element is (n-1)!. This means we have to keep on dividing k by (n-1)! and then use the remainder to find the next element in the permutation. We fix the first element and then find the k-th permutation of the remaining elements. We repeat this process until we have found the k-th permutation.

def kthPermutation(n, k):
      # Step 1: Precompute factorial (n-1)!
    fact = math.factorial(n - 1)

      # Step 2: Initialize list of available numbers
    nums = [i for i in range(1, n + 1)]

      # Step 3: Result string
    ans = ""

      # Step 4: Convert k to 0-based index
    k -= 1

      # Step 5: Build permutation one digit at a time
    while nums:
          # Find index of the digit in current nums
        idx = k // fact

          # Append chosen digit to result
        ans += str(nums[idx])

          # Remove chosen digit
        nums.pop(idx)

          # Stop if no digits left
        if not nums:
            break

          # Update k and factorial for next step
        k %= fact
        fact //= len(nums)

    return ans


  # Example Runs
print(kthPermutation(3, 4))   # "231"
print(kthPermutation(3, 6))   # "321"
print(kthPermutation(4, 17))  # "3412"

