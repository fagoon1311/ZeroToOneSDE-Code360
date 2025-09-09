#Problem: Given a linked list, remove the kth node from the end of the list and return its head.

# Approach1: The naive solution is to process all the nodes from the front side of the linked list and keep adding a node to the list. Now we can easily remove the Kth node from the end of the list by simply replacing the next pointer of the ('LENGTH' - 'K' - 1)th node (0-based indexing from start) of the list with the ('LENGTH' - 'K' + 1)th node. This way we can remove the Kth node from the end of the linked list. 

'''
    Time Complexity: O(N)
    Space Compexity: O(N)

    Where 'N' is the total nodes in Linked List.
'''

def removeKthNode(head, k):
    if head is None or k == 0:
        return head

    # It stores all the node of Linked List.
    nodeList = []

    # Creating temporory node.
    temp = head

    # Iterating the Linked List.
    while temp is not None:
        # Add current node to list
        nodeList.append(temp)

        temp = temp.next

    # If head of Linked List is the Kth node.
    if k == len(nodeList):
        next = head.next
        head.next = None
        head = next
    else:
        # Remove the Kth node from end.
        nodeList[len(nodeList) - k - 1].next = nodeList[len(nodeList) - k].next

    return head


# Approach2: By finding the length of the linked list, we can easily remove the Kth node from the end of the list by simply replacing the next pointer of the Length - kth node (0-based indexing from start) of the list with the Length - k + 1th node. This way we can remove the Kth node from the end of the linked list.

'''
    Time Complexity: O(N)
    Space Compexity: O(1)

    Where 'N' is the total nodes in Linked List.
'''

def lenLL(head):
    curr = head
    ans = 0

    while curr:
        ans += 1
        curr = curr.next

    return ans


def removeKthNode1(head, k):
    # Write your code here.
    l = lenLL(head)
    curr = head
    i = l - k
    if i == 0:
        return head.next
    while i > 1:
        curr = curr.next
        i -= 1


    if curr.next.next:
        curr.next = curr.next.next
    else:
        curr.next = None

    return head    


# Approach3: We can use two pointers to solve this problem. We can use one pointer to point to the head of the linked list and the other pointer to point to the Kth node from the end of the list. We move fast until it reaches k nodes apart. Then we move both pointers until fast reaches the end of the list. Then we remove the node that slow is pointing to.

def removeKthNode2(head, k):
  slow = fast = head

  # Move fast k steps ahead
  for _ in range(k):
      fast = fast.next
      if fast is None:   # means we are removing the head
          return head.next

  # Move both until fast reaches the last node
  while fast.next:
      slow = slow.next
      fast = fast.next

  # Remove K-th from end
  slow.next = slow.next.next
  return head
