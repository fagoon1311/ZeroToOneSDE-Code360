# Problem: Given two sorted Linked Lists merge them into a single LL.
# Solution: Use two pointers to merge the two LLs into the first LL. This is O(m + n) time complexity.
class Node:
  def __init__(self, data):
      self.data = data
      self.next = None

def sortTwoLists(first, second):
  # If either list is empty, return the other list
  if first is None:
      return second
  if second is None:
      return first
  # Create a new node to hold the merged list
  newNode = Node(-1)
  curr = newNode

  # Traverse both lists and compare the data of the nodes
  while first is not None and second is not None:
      # If the data of the first node is less than or equal to the data of the second node, add the first node to the merged list and move to the next node in the first list. Otherwise, add the second node to the merged list
      if first.data <= second.data:
          curr.next = first
          first = first.next
      else:
          curr.next = second
          second = second.next
      curr = curr.next

     # If one of the lists is empty, add the remaining nodes of the other list to the merged list
  if first is not None:
      curr.next = first
  if second is not None:
      curr.next = second

  return newNode.next