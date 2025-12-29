# Problem Statement: Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph. 
#A Directed Acyclic Graph (DAG) is a directed graph that contains no cycles.

#Topological Sorting of DAG is a linear ordering of vertices such that for every directed edge from vertex ‘u’ to vertex ‘v’, vertex ‘u’ comes before ‘v’ in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

# Solution 1: Using DFS

from os import *
from sys import *
from collections import *
from math import *

'''
Time Complexity: O(V + E)
Space Complexity: O(V + E)
'''

def dfs(node, visited, stack, adj):
  visited[node] = 1

  for n in adj[node]:
      if visited[n] == 0:
          dfs(n, visited, stack, adj)

  stack.append(node)


def topologicalSort(adj, v, e):
  # Write your code here
  stack = []
  visited = [0] * v

  adjL = [[] for _ in range(v)]

  for u, ve in adj:
      if u is not None and ve is not None:
          adjL[u].append(ve)

  for i in range(v):
      if visited[i] == 0:
          dfs(i, visited, stack, adjL)



  res = []

  while stack:
      res.append(stack.pop())

  return res


# Solution 2: Using BFS


def topologicalSort2(adj, v, e):
    # Write your code here
    adjL = [[] for _ in range(v)]
    for u, n in adj:
        if u is not None and n is not None:
            adjL[u].append(n)
    stack = []
    idg = [0] * v

    q = deque()
    for al in adjL:
        for n in al:
            idg[n] += 1

    for i in range(v):
        if idg[i] == 0:
            q.append(i)

    res = []
    j = 0

    while q:
        node = q.popleft()
        res.append(node)

        for i in adjL[node]:
            idg[i] -= 1
            if idg[i] == 0:
                q.append(i)

    return res
