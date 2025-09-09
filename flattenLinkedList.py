# You are given a linked list containing 'n' 'head' nodes, where every node in the linked list contains two pointers:

# (1) ‘next’ which points to the next node in the list

# (2) ‘child’ pointer to a linked list where the current node is the head.
# Each of these child linked lists is in sorted order and connected by 'child' pointer. Your task is to flatten this linked such that all nodes appear in a single layer or level in a 'sorted order'.

# -------------------------------------------------
#Solution 1:

# Naive Solution: We can store all the nodes in a list and then sort the list and then create a new linked list from the sorted list. 

# Time Complexity
# O((n * k) * (log(n * k))), where ‘n’ denotes the size of the linked list and ‘k’ is the average number of child nodes for each of the n nodes. Since we are taking all nodes data in an array and then sorting it so the total complexity will O(n * k) + O((n * k) * log(n * k))

# Space Complexity
# O(n * k), where ‘n’ denotes the size of the linked list and ‘k’ is the average number of child nodes for each of the n nodes. Since we are using an array to store all the nodes of the linked list, and we are creating a new linked list to again store all the nodes, so the effective space complexity would be O(n * k) + O(n * k) = O(n * k).

# --------------------------------------------------

#Solution 2: Pre-requisite: Merge two sorted linked lists.
# We can use the merge two sorted linked lists approach to solve this problem. We can use a recursive function to merge two sorted linked lists. The base case is when one of the linked lists is empty. We return the other linked list. 
# we use a helper merge function to merge two sorted linked lists.
# We use a recursive function to flatten the linked list. The base case is when the linked list is empty. We return the linked list.

class Node:
  def __init__(self, val=0, next=None, child=None):
      self.data = val
      self.next = next
      self.child = child

# Don't change the code above.

def merge(list1, list2):
  # A dummy node to store the result  
  dummy = Node(-1)
    # A tail node to record the last node
  res = dummy
    
# We iterate over the two linked lists and compare the data of the nodes. We add the smaller node to the result linked list and move the pointer of the linked list that we added the node from. We repeat this until we reach the end of one
  while list1 and list2:
      if list1.data < list2.data:
          res.child = list1
          res = list1
          list1 = list1.child

      else:
          res.child = list2
          res = list2
          list2 = list2.child
      res.next = None

  if list1:
      res.child = list1
  else:
      res.child = list2

  return dummy.child


def flattenLinkedList(head: Node) -> Node:
  if head is None or head.next is None:
      return head

  mergedhead = flattenLinkedList(head.next)
  return merge(head, mergedhead)


