#Problem Statement: Given a binary tree, print the top view of it. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top from the left side to the right side. Example: 

 #    1
 #  /   \
 # 2     3
 #  \   / \
 #   4 5   6
 #      \
 #       7

# then res would look like [2, 1, 3, 6]

# Solution: We can use level order traversal to solve. We can maintain a map that stores the horizontal distance of each node from the root. If a horizontal distance is already present in the map, we ignore it. We start with root at horizontal distance 0. We traverse the left subtree and decrement the horizontal distance by 1. We traverse the right subtree and increment the horizontal distance by 1. We print the nodes in the map in the order of their horizontal distance.

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)

# Following is the TreeNode class structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def getTopView(root):
    # Write your code here.
    if not root:
        return []
    hd = 0
    seen = {}
    res = []

    minhd, maxhd = 0, 0
    q = [(root, hd)]
    while len(q) > 0:
        node, hd = q.pop(0)
        if hd not in seen:
            seen[hd] = node.val

        minhd = min(minhd, hd)
        maxhd = max(maxhd, hd)

        if node.left:
            q.append((node.left, hd - 1))

        if node.right:
            q.append((node.right, hd + 1))

    for hd in range(minhd, maxhd + 1):
        res.append(seen[hd])

    return res

    pass

# Taking input.
def takeInput():

    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if(leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if(rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)

        index += 1

    return root

# Printing the tree nodes.
def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()


# Main.
T = 1
for i in range(T):
    root = takeInput()
    ans = getTopView(root)
    printAns(ans)