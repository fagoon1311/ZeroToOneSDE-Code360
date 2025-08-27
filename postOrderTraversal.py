#Problem Description: Given a binary tree, return the postorder traversal of its nodes' values.

# SOlution: Recursive -> O(n) time complexity, O(n) space complexity. For each node, recursively traverse the left subtree, then the right subtree, then add the node's value to the result list.

def postOrderTraversal(root):
  if root is None:
    return []
  return postOrderTraversal(root.left) + postOrderTraversal(root.right) + [root.val]

