# Given a graph with starting vertex as 0 print bfs of the graph.

from typing import List

def bfsTraversal(n: int, adj: List[List[int]]) -> List[int]:
    q = [0]
    res = []
    visited = [0 for i in range(n)]
    visited[0] = 1

    while q:
        curr = q.pop(0)
        res.append(curr)
        for item in adj[curr]:
            if not visited[item]:
                q.append(item)
                visited[item] = 1

    return res

'''
Time Complexity: 
Construction of visited array takes O(n) time.
Each Pop operation takes O(n) time so for each n element it takes O(n^2) time.
Visiting all nodes takes n time
checking all edges takes m time
So overall time complexity is O(n^2 + m)

We can optimize by using deque instead of list for queue. That makes popleft operation O(1) instead of O(n).
So overall time complexity is O(n + m)


Space Complexity: O(n + m)

'''