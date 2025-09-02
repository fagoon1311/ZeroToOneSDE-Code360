# Problem: Given a string, print all permutations of the string.
# If we have n characters in a string, there are n! permutations of the string.


#Solution1: We use a map to keep track of which characters we have already used in the current permutation. We use a recursive function to generate the permutations. The base case is when the length of the current permutation is equal to the length of the string. We then print the current permutation. We then

def findPerms(ds, s, ans, freq):
  # Base case is when our data Structure is of same length as of our string.
  # this means we have completed one permutation of string and we can append it to our ans.
  if len(ds) == len(s):
    print(ds)
    #ans.append(ds) # This will be empty at the end of the recursion. because it is a reference to the same object that we are passing in the function. and we are popping from it so its empty at the end of the recursion. instead we shoud store a shallow copy of ds in ans.
    ans.append(ds[:])
    return

  # We iterate over the string and if the character is not in the map we add it to the map and call the function again.
  for i in range(len(s)):
    if not freq[i]:
      ds.append(s[i])
      freq[i] = 1
      findPerms(ds, s, ans, freq)
      freq[i] = 0
      ds.pop()




def printPermutations(s):
  # Write your code here.
  ans = []
  ds = []
  freq = [0 for _ in range(len(s))]
  findPerms(ds, s, ans, freq)
  print(ans)




# []
# ├── ['a'], freq=[1,0,0]
# │   ├── ['a','b'], freq=[1,1,0]
# │   │   └── ['a','b','c'], freq=[1,1,1] ✅
# │   └── ['a','c'], freq=[1,0,1]
# │       └── ['a','c','b'], freq=[1,1,1] ✅
# ├── ['b'], freq=[0,1,0]
# │   ├── ['b','a'], freq=[1,1,0]
# │   │   └── ['b','a','c'], freq=[1,1,1] ✅
# │   └── ['b','c'], freq=[0,1,1]
# │       └── ['b','c','a'], freq=[1,1,1] ✅
# └── ['c'], freq=[0,0,1]
#     ├── ['c','a'], freq=[1,0,1]
#     │   └── ['c','a','b'], freq=[1,1,1] ✅
#     └── ['c','b'], freq=[0,1,1]
#         └── ['c','b','a'], freq=[1,1,1] ✅




#_______________________Sol1 ends _______________________________

# Solution2: We will not use any extra data structure to keep track of the characters we have already used. Instead we will swap the characters in the string and then call the function again. We will swap the characters back to their original position after the function call. This is because we are passing the string by reference and we want to make sure that the string is in its original state after the function call.

def findPerms2(ind, s, ans):
  # Base case is when our index is equal to the len of the string.
  if ind == len(s):
    ds = []
    for i in range(len(s)):
      ds.append(s[i])
    ans.append(ds)
    return

  # We iterate over the string and swap the characters and call the function again.
  for i in range(ind, len(s)):
    s[ind], s[i] = s[i], s[ind]
    findPerms2(ind + 1, s, ans)
    # We swap the characters back to their original position.
    s[ind], s[i] = s[i], s[ind]

def printPermutations2(s):
  ans = []
  sarr = list(s)
  findPerms2(0, sarr, ans)
  print(ans)


printPermutations2("abc")


# ind=0: ['a','b','c']
# ├── swap(0,0) → ['a','b','c']
# │   ├── swap(1,1) → ['a','b','c'] → PERM
# │   └── swap(1,2) → ['a','c','b'] → PERM
# │
# ├── swap(0,1) → ['b','a','c']
# │   ├── swap(1,1) → ['b','a','c'] → PERM
# │   └── swap(1,2) → ['b','c','a'] → PERM
# │
# └── swap(0,2) → ['c','b','a']
#     ├── swap(1,1) → ['c','b','a'] → PERM
#     └── swap(1,2) → ['c','a','b'] → PERM
