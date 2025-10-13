# Problem Statement: Given a binary tree, print the bottom view of it. The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom from the left side to the right side. If two nodes are at the same horizontal distance from the root, then the node that is at the right is considered to be in the bottom view.



# Solution: We can use level order traversal to solve. We can maintain a map that stores the horizontal distance of each node from the root. If a horizontal distance is already present in the map, we update it. We start with root at horizontal distance 0. 

'''
TC: O(nlogn) where n is the number of nodes in the tree)

SC: O(n)

'''
class BinaryTreeNode:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

  def __repr__(self, level=0, prefix="Root: "):
      ret = "  " * level + prefix + repr(self.data) + "\n"
      if self.left:
          ret += self.left.__repr__(level + 1, "L--- ")
      if self.right:
          ret += self.right.__repr__(level + 1, "R--- ")
      return ret

# Example Usage
root = BinaryTreeNode(10)
root.left = BinaryTreeNode(5)
root.right = BinaryTreeNode(20)
root.left.left = BinaryTreeNode(3)
root.left.right = BinaryTreeNode(7)
root.right.right = BinaryTreeNode(25)


print(root)


def getBottomView(root):
    seen = {}
    q = [(root, 0)]
    hd = 0
    res = []

    while len(q) > 0:
        node, hd = q.pop(0)
        seen[hd] = node.data

        if node.left:
            q.append([node.left, hd - 1])

        if node.right:
            q.append([node.right, hd + 1])

        
    for item in sorted(seen.keys()):
        res.append(seen[item])

    return res

print(getBottomView(root))

# {0: 7, -1: 5, 1: 20, -2: 3, 2: 25}


