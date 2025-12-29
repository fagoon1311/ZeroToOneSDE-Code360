# Problem Statement: Given an undirected graph, check if there is a cycle in the graph.

# Solution 1: Using BFS -> We traverse in forward direction from the source node. We also keep track of the parent node. We use a queue to traverse and we also keep a visited array to keep track of visited nodes. If we encounter a node which is already visited and it is not the parent node, then there is a cycle.

'''
TC - 0(n + 2e) + 0(n) = 0(n + e)
SC - 0(n) + 0(n) = 0(n)
'''

from collections import deque

def checkCycle(src, adjacency_list, visited):
    q = deque()
    q.append((src, -1))
    visited[src] = 1
    while q:
        node, parent = q.popleft()

        for an in adjacency_list[node]:
            if visited[an] == 0:
                visited[an] = 1
                q.append((an, node))

            elif parent != an:
                return True

    return False

def cycleDetection(edges, n, m):

    # Write your code here.
    # Return "Yes" if cycle is present in the graph else return "No".

    adjacency_list = [[] for _ in range(n + 1)]

    visited = [0 for _ in range(n + 1)]
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)


    for i in range(1, n + 1):
        if visited[i] == 0:
            if checkCycle(i, adjacency_list, visited):
                return "Yes"

    return "No"


# Soluton 2: Using DFS -> We traverse in forward direction from the source node. We also keep track of the parent node. 

'''
TC - 0(n + 2e) + 0(n) = 0(n + e)
SC - 0(n) + 0(n) = 0(n)

'''


def checkCycle2(src,parent, adjacency_list, visited):
    visited[src] = 1

    for an in adjacency_list[src]:
        if visited[an] == 0:
            if checkCycle2(an,src, adjacency_list, visited):
                return True

        elif an != parent:
            return True

    return False

def cycleDetection2(edges, n, m):

    # Write your code here.
    # Return "Yes" if cycle is present in the graph else return "No".

    adjacency_list = [[] for _ in range(n + 1)]

    visited = [0 for _ in range(n + 1)]
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)


    for i in range(1, n + 1):
        if visited[i] == 0:
            if checkCycle2(i, -1,  adjacency_list, visited):
                return "Yes"

    return "No"


