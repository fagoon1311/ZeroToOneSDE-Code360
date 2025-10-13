# Statement: Given two binary trees, check if they are identical or not.

# Solution1: Level Order Traversal
# We will use level order traversal to traverse both trees. If at any point the nodes are not equal, we will return false. If we reach the end of both trees, we will return true.

'''
    Time complexity: O( max(M, N) ) 
    Space complexity: O( max(M, N) )

    M and N are number of nodes in binary tree 1 and binary tree 2 respectively.
'''
from typing import List


class BinaryTreeNode:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

def createLevelOrder(root: BinaryTreeNode) -> List[int]:

    # Res will store level order traversal of the tree.
    res = []

    if root is None:
        res.append(-1)
        return res

    # Using queue to implement level order traversal.
    que = []

    que.append(root)

    res.append(root.data)

    while(len(que)>0):

        first = que.pop(0)

        # Push the left child into queue.
        if first.left!=None:
            que.append(first.left)
            res.append(first.left.data)

        else:
            # Push -1 for null node.
            res.append(-1)

        # Push the right child into queue.   
        if first.right!=None:
            que.append(first.right)
            res.append(first.right.data)

        else:
            # Push -1 for null node.
            res.append(-1)

    return res




def identicalTrees(root1: BinaryTreeNode, root2: BinaryTreeNode) -> bool:

    arr1 = createLevelOrder(root1)

    arr2 = createLevelOrder(root2)

    if len(arr1)!=len(arr2):
        return False

    for i in range(len(arr1)):

        if arr1[i]!=arr2[i]:
            return False

    return True


#SOlution2: Recursive Approach

'''
    Time complexity: O(min(M, N)) 
    Space complexity: O(min(H1, H2)

    M and N are number of nodes and H1 and H2 are heights of binary tree 1 and binary tree 2 respectively.
'''

class BinaryTreeNode:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


def identicalTrees1(root1: BinaryTreeNode ,root2: BinaryTreeNode) -> bool:

    # If both are NULL trees, they are identical. 

    if root1 is None and root2 is None:
        return True

    # If any one of the trees is NULL, they are not identical.

    if root1 is None or root2 is None:
        return False

    # Check if root's data of both the trees is same. 
    # Recursively check if left subtree and right subtree of both trees is identical. 
    # Return true only if all conditions satisfy.

    return ((root1.data == root2.data) and 
           identicalTrees1(root1.left,root2.left) and 
           identicalTrees1(root1.right,root2.right))