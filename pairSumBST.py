from os import *
from sys import *
from collections import *



# Problem Statement: Given the root of a binary search tree and an integer k, return true if a pair exists in the BST such that their sum equals k. Note that each node may only be used once.

# Solution1: For each node in the BST, we will search for the value k - node.val in the BST. If we find it, we return true. Otherwise, we return false.

'''
Time Complexity: O(n^2) where n is the number of nodes in the BST.
Space Complexity: O(n)

'''

def dfs(root, target, ignoreNode):
    if root is None:
        return False

    if root.data == target and root != ignoreNode:
        return True

    if root.data < target:
        return dfs(root.right, target, ignoreNode)

    else:
        return dfs(root.left, target, ignoreNode)


def checkPair(root, target, bstroot):
    if root is None:
        return False

    comp = target - root.data

    if dfs(bstroot, comp, root):
        return True

    return checkPair(root.left, target, bstroot) or checkPair(root.right, target, bstroot)


def pairSumBST(root, k):
    return checkPair(root, k, root)



# Solution2: We can use inorder traversal to get the sorted array and then use two pointer approach to find the pair.

'''
Time Complexity: O(n) where n is the number of nodes in the BST.
Space Complexity: O(n)
'''
def inorder(root, arr):
  if root is None:
    return 

  inorder(root.left, arr)
  arr.append(root.data)
  inorder(root.right, arr)

def findPair(arr, target):
  l, r = 0, len(arr) - 1
  while l < r:
    if arr[l] + arr[r] == target:
      return True
    elif arr[l] + arr[r] < target:
      l += 1

    else:
      r -= 1
  return False


def pairSumBST2(root, k):
  sortedarr = []
  inorder(root, sortedarr)
  return findPair(sortedarr, k)


# SOlution3: We can use a set to store values of nodes. We use DFS to traverse the BST. For each node, we check if k - node.val is in the set. If it is, we return true. Otherwise, we add node.val to the set and continue.
'''
Time Complexity: O(n) where n is the number of nodes in the BST.
Space Complexity: O(n)
'''

def pairSumBST3(root, k):
  seen = set()
  def dfs(root):
    if root is None:
      return False
    if k - root.data in seen:
      return True
    seen.add(root.data)

    return dfs(root.left) or dfs(root.right)
  return dfs(root)