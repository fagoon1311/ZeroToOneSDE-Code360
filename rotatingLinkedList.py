# Rotate a linked list by k places to the right.

# Brute Force Solution:
# Create a array of list node data. Rotate the array and replace the data in the LinkedLISt.

'''
Time Complexity: O(n)
Space Complexity: O(n)

'''
class Node:
  def __init__(self, val, next=None):
      self.data = val
      self.next = next


def rotate(head: Node, k: int) -> Node:
  def rotatearr(arr, k):
      n = len(arr)
      k %= n

      def rev(a, l, r):
          while l < r:
              a[l], a[r] = a[r], a[l]
              l += 1
              r -= 1

      rev(arr, 0, n - 1)
      rev(arr, 0, k - 1)
      rev(arr, k, n - 1)

  ll = []

  curr = head
  while curr:
      ll.append(curr.data)
      curr = curr.next

  rotatearr(ll, k)

  temp = head
  i = 0
  while temp:
      temp.data = ll[i]
      i += 1
      temp = temp.next

  return head



# Optimal solution: We find tail and length.  Then we find the new tail and new head. We connect the new tail to head and new head to None.
def rotate(head: Node, k: int) -> Node:
    length = 1
    tail1 = head
    tail2 = head

    while tail1.next:
        tail1 = tail1.next
        length += 1


    k %= length

    if k == 0:
        return head

    tail1.next = head

    tail2 = head

    for i in range(length - k - 1):
        tail2 = tail2.next

    newHead = tail2.next
    tail2.next = None

    return newHead



