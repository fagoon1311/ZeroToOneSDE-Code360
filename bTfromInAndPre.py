from typing import List
# Problem Statement: Given the inorder and preorder traversal of a binary tree, construct the binary tree. You can assume that duplicates do not exist in the tree.

# Naive Solution: The main idea is to use Recursion. We know that first node of preorder traversal is the root. We can find the index of this root in inorder traversal. All nodes to the left of this index in inorder traversal are in left subtree and all nodes to the right are in right subtree. We can recursively construct the left and right subtree.


'''
TC: O(n^2) where n is the number of nodes in the tree)
SC: O(n)
'''
# Following is the structure of Tree Node
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def buildBinaryTree(preorder: List[int], inorder: List[int]) -> TreeNode:
  # Write your code here.
    def build(inorder, preorder):
        if not preorder or not inorder:
            return None

        root_val = preorder[0]

        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        root.left = build(inorder[:mid], preorder[1: mid+1])
        root.right = build(inorder[mid + 1:], preorder[mid + 1:])

        return root

    return build(inorder, preorder)


# Optimized Solution: Instead of finding the index of root in inorder traversal every time, we can use a map to store the index of each node in inorder traversal. This will reduce the time complexity to O(n).

def buildBinaryTree(preorder: List[int], inorder: List[int]) -> TreeNode:
  # Map each value to its index in inorder for O(1) lookup
  inorder_index = {val: idx for idx, val in enumerate(inorder)}
  preorder_index = [0]  # mutable index so recursion can update it

  def build(left, right):
      if left > right:
          return None

      # Pick root value from preorder using preorder_index
      root_val = preorder[preorder_index[0]]
      preorder_index[0] += 1
      root = TreeNode(root_val)

      # Build left & right subtrees using inorder boundaries
      root.left = build(left, inorder_index[root_val] - 1)
      root.right = build(inorder_index[root_val] + 1, right)

      return root

  return build(0, len(inorder) - 1)
