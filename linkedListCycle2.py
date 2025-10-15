# Problem Statement - Return the node where the cycle begins. If there is no cycle, return null.

# Solution - 1: Hash Set  O(n) time and O(n) space

'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def firstNode(head):
    visited = {}

    curr = head
    pos = 0

    while curr and curr.next:
        if curr in visited:
            return visited[curr]

        else:
            visited[curr] = pos

            curr = curr.next
            pos += 1

    return -1


# Solution - 2: Flod's Cycle Detection Algorithm  O(n) time and O(1) space
# Two pointers, slow and fast. Slow moves one step at a time, fast moves two steps at a time. When they meet, there is a cycle. To  find the start of the cycle, move one pointer to the head and move both pointers one step at a time. When they meet, that's the start of the cycle.


def firstNode2(head):
  slow = fast = head
  curr = head
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

      if slow == fast:
          while curr != slow:
              slow = slow.next
              curr = curr.next
          return slow

  return None