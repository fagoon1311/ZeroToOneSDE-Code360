# Problem Statement: Given a binary tree, find the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

#Brute force Solution: We can use a recursive function to find the diameter of the tree. The base case is when the node is None. We return 0. We use a helper function to find the height of the tree. for each node we find the height of the left and right subtree. The diameter of the tree is the maximum of left height + right height + 1.
# Time Complexity: O(n^2) because we are finding the height of the tree for each node.

def findLeftHeight(root):
  if root is None:
    return 0
  return 1 + findLeftHeight(root.left)

def findRightHeight(root):
  if root is None:
    return 0
  return 1 + findRightHeight(root.right)
  

