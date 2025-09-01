# Problem - Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Solution - Use a doubly linked list to keep track of the order of the elements. Use a hashmap to keep track of the key-value pairs. When a key is accessed, move it to the front of the list. When a key
# is added, add it to the front of the list. When the cache is full, remove the last element from the list and the hashmap.


class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.prev = self.next = None

class LRUCache:
  def __init__(self, capacity):
    self.capacity = capacity
    self.cache = {}  # maps key -> Node

    # Dummy nodes (left = LRU, right = MRU)
    self.left, self.right = Node(0, 0), Node(0, 0)
    self.left.next, self.right.prev = self.right, self.left

  # Remove a node from DLL
  def remove(self, node):
    prev, nxt = node.prev, node.next
    prev.next, nxt.prev = nxt, prev

  # Insert node at MRU position (just before right)
  def insert(self, node):
    prev, nxt = self.right.prev, self.right
    prev.next = nxt.prev = node
    node.prev, node.next = prev, nxt

  def get(self, key):
    if key in self.cache:
      node = self.cache[key]
      self.remove(node)
      self.insert(node)
      return node.value
    return -1

  def put(self, key, value):
    if key in self.cache:
      self.remove(self.cache[key])
    self.cache[key] = Node(key, value)
    self.insert(self.cache[key])

    if len(self.cache) > self.capacity:
      # remove from DLL + delete from hashmap
      lru = self.left.next
      self.remove(lru)
      del self.cache[lru.key]
