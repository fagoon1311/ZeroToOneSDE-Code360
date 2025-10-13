# Problem Statement: You are given a string 'S'. Your task is to partition 'S' such that every substring of the partition is a palindrome. You need to return all possible palindrome partitioning of 'S'. Note: A substring is a contiguous segment of a string.

# Solution: The main idea behind this approach is to use backtracking. We start by checking if the current substring is a palindrome. If it is, we add it to the current path and recursively call the function for the remaining substring. If it is not, we just return. We keep doing this until we reach the end of the string. If we reach the end of the string, we add the current path to the result. 

# Example s = 'aab' -> [['a', 'a', 'b'], ['aa', 'b']]

# Start: i=0, path=[]
# ├── "a" → i=1, path=["a"]
# │   ├── "a" → i=2, path=["a", "a"]
# │   │   └── "b" → i=3 → add ["a", "a", "b"]
# │   └── "ab" → not palindrome
# ├── "aa" → i=2, path=["aa"]
# │   └── "b" → i=3 → add ["aa", "b"]
# └── "aab" → not palindrome


# Example s = 'baab' -> [['b', 'a', 'a', 'b'], ['b', 'aa', 'b'], ['baab']]

 #                  ""
 #                   |
 #                ┌──┴────┐
 #               "b"     "ba" ✘
 #                |      
 #           ┌────┴───────┐
 #          "a"          "aa"
 #           |             |
 #     ┌─────┴─────┐       |
 #    "a"         "ab"✘   "b"
 #     |                   |
 #   "b"                  ✅ ["b", "aa", "b"]
 #     |
 #    ✅ ["b", "a", "a", "b"]

 # "baa" ✘       "baab"
 #                    |
 #                  ✅ ["baab"]


def isPal(s, l, r):
  while l <= r:
      if s[l] != s[r]:
          return False
      l += 1
      r -= 1
  return True

# Recursive backtracking function
def func(s, i, res, path):
  if i == len(s):
      res.append(path[:])
      return

  for idx in range(i, len(s)):
      if isPal(s, i, idx):
          path.append(s[i:idx+1])
          func(s, idx+1, res, path)
          path.pop()

# Main partition function
def partition(s):
  res = []
  func(s, 0, res, [])
  return res

