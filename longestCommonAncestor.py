# Problem:  Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# The lowest common ancestor is the lowest node in the tree that has both nodes as descendants.

'''
Algorithm Idea:
• Traverse the tree using recursion.
• If the current node matches either of the given values, return it.
• Recursively search in left and right subtrees.
• If both sides return a node, the current node is the LCA.
• Otherwise, return the non-null result.
Example Tree:
    3
   / \
  5   1
    /   \
   6     2
Dry Run for x = 6 and y = 2:
1. Start at node 3 → not a match → search left and right.
2. Node 5 → no match → returns None.
3. Node 1 → not a match → search left and right.
4. Node 6 → match found → return node 6.
5. Node 2 → match found → return node 2.
6. At node 1 → both left and right returned values → node 1 is LCA.
7. Result propagates up to root.
Final Answer: Lowest Common Ancestor = 1
Time Complexity: O(n)
Space Complexity: O(h), where h is height of the tree

'''

def lowestCommonAncestor(root, x: int, y: int) -> int:

  def lca(node):
      if node is None:
          return None

      if node.data == x or node.data == y:
          return node

      left = lca(node.left)
      right = lca(node.right)

      if left and right:
          return node

      return left if left else right

  ans = lca(root)
  return ans.data if ans else -1
