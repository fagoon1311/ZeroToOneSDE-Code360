# Problem Statement: Given a string s, return the longest palindromic substring in s.

# Solution1: Brute Force: We can use two nested loops to generate all possible substrings and check if they are palindromic. If they are, we update the longest palindromic substring.

'''
Time Complexity: O(n^3) where n is the length of the string.
The brute-force solution for finding the longest palindromic substring has a time complexity of O(n³), not O(n⁴) as it might initially seem. The algorithm uses two nested loops to generate all possible substrings of the input string. The outer loop runs O(n) times, and for each iteration, the inner loop also runs up to O(n) times, resulting in O(n²) substring combinations in total. For each substring, the code performs two operations: slicing the string to create a new substring (s[i:j]) and checking whether that substring is a palindrome. Both slicing and palindrome checking operate in O(k) time, where k is the length of the substring, which in the worst case is O(n). Importantly, these two operations are sequential, not nested, so their time complexities add up rather than multiply — that is, O(n) + O(n) = O(n), not O(n²). Therefore, for each of the O(n²) substring combinations, the total time spent is O(n), resulting in an overall time complexity of O(n³).

Space Complexity: O(1)

'''

def isPal(s: str) -> bool:
  l = 0
  r = len(s) - 1

  while l <= r:
      if s[l] != s[r]:
          return False

      else:
          l += 1
          r -= 1

  return True



def longestPalinSubstring(str: str) -> str:
  currLen = 0
  res = ""
  l = len(str)
  for i in range(l):
      for j in range(i + 1, l + 1):
          curr = str[i:j]
          if isPal(curr) and len(curr) > currLen:
              res = curr
              currLen = len(curr)

  return res



# Solution2: Expand around center for each character in the string. For each character there are two cases: the character itself is the center or the character and the next character are the center. We will check both cases and update the longest palindromic substring.

'''
Time Complexity: O(n^2) where n is the length of the string.
Space Complexity: O(1)
'''

def expand(s: str, l:int, r:int) -> str:
  while l >= 0 and r < len(s) and s[l] == s[r]:
      l -= 1
      r += 1

  return s[l + 1: r]

def longestPalinSubstring1(str: str) -> str:
  l = len(str)
  res = ""
  for i in range(l):
      odd = expand(str, i, i)
      even = expand(str, i, i + 1)

      if len(odd) > len(res):
          res = odd

      if len(even) > len(res):
          res = even

  return res




