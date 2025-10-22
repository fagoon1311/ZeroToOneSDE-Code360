# Problem - Given a string return the length of lngest substring without repeating chars.

# Solution 1 - Brute Force

''''
    Time Complexity - O(N^3)
    Space Complexity - O(N)

    where N is the length of the string.
'''

def allUnique(wrapper, start, end) :

    # for storing every character of string
    Set = set()
    for i in range(start, end) :
        ch = wrapper[0][i]

        # if a character is already there then we have a found duplicates
        # so we need to return false
        if ch in Set :
            return False

        Set.add(ch)

    return True

def uniqueSubstrings(input) :

    n = len(input)
    ans = 0

    # check for every possible substring
    # creating the wrapper around the string 
    # so that on every function call string is not copied
    wrapper = []
    wrapper.append(input)
    for i in range(n) :
        for j in range(i+1, n+1) :

            # if substring contains unique characters then update the maximum.
            if (allUnique(wrapper, i, j)) :
                ans = max(ans, j - i)

    return ans


# Solution 2 - Sliding Window

'''
Time Comlexity: O(n)
Space Complexity: O(k) where k is the size of the set.
'''

def uniqueSubstrings1(inp) :
  # Write your code here.
  l, r = 0, 0
  seen = set()
  ans = 0
  while l < len(inp) and r < len(inp):
      if inp[r] not in seen:
          seen.add(inp[r])
          ans = max(ans, r - l + 1)
          r += 1

      else:
          seen.remove(inp[l])
          l += 1

  return ans
