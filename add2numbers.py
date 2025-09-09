# You are given two non-negative numbers 'num1' and 'num2' represented in the form of linked lists.The digits in the linked lists are stored in reverse order, i.e. starting from least significant digit (LSD) to the most significant digit (MSD), and each of their nodes contains a single digit. Calculate the sum of the two numbers and return the head of the sum list.

# Approach 1: We create a new linked list to store the sum of the two numbers. We iterate through the two linked lists and add the digits of the two numbers. If the sum is greater than 9, we carry over the 1 to the next digit. We continue this until we reach the end of the two linked lists. If one of the linked lists is longer than the other, we continue to add the digits of the longer linked list to the sum. If there is a carry over at the end of the iteration, we add a new node to the sum linked list with the value of the carry over.

class Node:
  def __init__(self, data=0, next=None):
      self.data = data
      self.next = next

def addTwoNumbers(head1: Node, head2: Node) -> Node:
  resHead = Node(0)
  curr = resHead
  carry = 0
  while head1 or head2 or carry != 0:
      val1 = head1.data if head1 else 0
      val2 = head2.data if head2 else 0
      currSum = val1 + val2 + carry
      carry = currSum // 10
      newNode = Node(currSum % 10)
      curr.next = newNode
      curr = newNode
      head1 = head1.next if head1 else None
      head2 = head2.next if head2 else None

  return resHead.next


# Approach 2: Can we eliminate the extra space used to store the result linked list? Yes, we can. We can use the input linked lists to store the result.


class Node:
  def __init__(self, data=0, next=None):
      self.data = data
      self.next = next

'''
  Time Complexity: O('m' + 'n')
  Space Complexity: O(1)

  Where 'm' and 'n' are the lengths of the linked lists.
'''

def addTwoNumbers2(head1: Node, head2: Node) -> Node:
  # 'NODE1' and 'NODE2' point to the current node of the first and second list, respectively.
  node1 = head1
  node2 = head2

  prev = None

  # 'SUM' and 'CARRY' store the sum and carry generated in the current iteration.
  sum = carry = 0

  while(node1 != None and node2 != None):
      # Add the values in the current nodes along with the carry.
      sum = node1.data + node2.data + carry

      # Store the next node of the sum list in the current node of the first linked list.
      node1.data = sum % 10

      # Get the new carry.
      carry = sum // 10

      # Keep track of the previous node.
      prev = node1

      # Move to the next node
      node1 = node1.next
      node2 = node2.next

  # If there are remaining digits in any one of the lists, add them to the sum list.
  if(node1 != None or node2 != None):
      if (node2 != None):
          prev.next = node2

      node1 = prev.next

      while(node1 != None):
          # Add the values in the current node along with the carry.
          sum = node1.data + carry

          # Store the next node of the sum list in the current node of the first linked list.
          node1.data = sum % 10

          # Get the new carry.
          carry = sum // 10

          # Keep track of the previous node.
          prev = node1

          # Move to the next node
          node1 = node1.next

  if(carry > 0):
      # Carry is generated from the last iteration. So, add a new node.
      prev.next = Node(carry)

  # Return the head of the sum list.
  return head1



