from collections import deque
# Problem Statement: Given a binary tree, return the vertical order traversal of the values of the nodes of the given tree.

# For each node at position (X, Y), (X-1, Y-1) will be its left child position while (X+1, Y-1) will be the right child position.

# Running a vertical line from X = -infinity to X = +infinity, now whenever this vertical line touches some nodes, we need to add those values of the nodes in order starting from top to bottom with the decreasing ‘Y’ coordinates.

# Note:
# If two nodes have the same position, then the value of the node that is added first will be the value that is on the left side.

# Example:
 #     1
 #    / \
 #   2   3
 #  / \   \
 # 4   5   6
# O/P = [4, 2, 1, 5, 3, 6]

# Approach1 : We can create a map that has horizontal distances as keys and nodes at each horizontal distance as values. We can use BFS to traverse the tree and keep track of the horizontal distance of each node. We can then sort the map by keys and print the values.

'''
Time Complexity: O(n log n)
The time complexity of the verticalOrderTraversal function can be broken down into distinct steps. First, the BFS traversal visits each node exactly once, which takes O(N) time. While traversing, we insert values into a dictionary keyed by horizontal distance, and since dictionary lookups and insertions take constant time on average, this step remains O(N) overall. Next, we sort the keys of the dictionary, and since the number of unique keys (horizontal distances) can be at most N, this step requires O(N log N) time in the worst case. After sorting, we build the result list by appending each node’s data once, which adds another O(N). Combining these, the overall time complexity becomes O(N log N). The space complexity is O(N) as well, since the queue, dictionary, and result list together may store up to N elements.

Space Complexity: O(n)
'''
def verticalOrderTraversal(root):
  res = []
  hd = 0
  q = deque([(root, hd)])
  level = {}

  while len(q) > 0:
      currNode, currHd = q.popleft()

      if currHd in level:
          level[currHd].append(currNode.data)

      else:
          level[currHd] = [currNode.data]


      if currNode.left:
          q.append((currNode.left, currHd - 1))

      if currNode.right:
          q.append((currNode.right, currHd + 1))

  for key in sorted(level.keys()):
      for item in level[key]:
          res.append(item)

  return res



# Optimizing Approach: We can eliminate the need to sort keys of our map by keeping track of minleft and maxright values. We can run a loop then to get values.

def verticalOrderTraversal2(root):
  res = []
  hd = 0
  q = deque([(root, hd)])
  minL, maxR = 0, 0
  level = {}

  while len(q) > 0:
      currNode, currHd = q.popleft()

      minL = min(minL, currHd)
      maxR = max(maxR, currHd)

      if currHd in level:
          level[currHd].append(currNode.data)

      else:
          level[currHd] = [currNode.data]


      if currNode.left:
          q.append((currNode.left, currHd - 1))

      if currNode.right:
          q.append((currNode.right, currHd + 1))

  for i in range(minL, maxR + 1):
      for item in level[i]:
          res.append(item)

  return res


