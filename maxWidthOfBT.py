# Problem -  Given the root of a binary tree, return the maximum width of the tree.
# There a 2 ways max width can be defined:
# 1. Maximum width is the maximum no. of nodes at any level.
# 2. Maximum width is the max no. of nodes between two end nodes at any level despiite null nodes in between.
# Write for both 2 cases.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
Solution for case 1
TC - O(n)
SC - O(n)

'''

def getMaxWidth(root):
  if root is None:
      return 0

  q = deque([root])
  ans = 0

  while q:
      size = len(q)
      ans = max(ans, size)

      for _ in range(size):
          node = q.popleft()

          if node.left:
              q.append(node.left)
          if node.right:
              q.append(node.right)

  return ans


'''
Solution for case 2
TC - O(n)
SC - O(n)
'''
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        ans = 0
        q = deque([(root, 0)])
        while q:
            size = len(q)
            mini = q[0][1]
            for i in range(size):
                node, idx = q.popleft()
                currIdx = idx - mini

                if i == 0:
                    first = currIdx
                if i == size - 1:
                    last = currIdx
                if node.left:
                    q.append((node.left, currIdx * 2 + 1))
                if node.right:
                    q.append((node.right, currIdx * 2 + 2))

            ans = max(ans, last - first + 1)
        return ans

