# Problem Statement: Given a BST and a key, find the inorder predecessor and successor of the key in the BST.
# The predecessor of a node X is the largest node in the BST that is smaller than X.
# The successor of a node X is the smallest node in the BST that is larger than X.


'''
 Time Complexity: O(n)
 Space Complexity: O(n)
 
 '''
def inorder(root, arr):
  if root is None:
      return

  inorder(root.left, arr)
  arr.append(root.data)
  inorder(root.right, arr)

def predecessorSuccessor(root, key):
  ino = []
  inorder(root, ino)
  p, s = -1, -1

  for i in range(len(ino)):
      if ino[i] < key:
          p = ino[i]

      elif ino[i] > key:
          s = ino[i]
          break

  return p, s