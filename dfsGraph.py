'''
Time Complexity: O(V + E)
Space Complexity: O(V + E)
'''


from typing import List

def depthFirstSearch(V: int, E: int, GRAPH: List[List[int]]):
    # Build adjacency list
    adj = [[] for _ in range(V)]
    for u, v in GRAPH:
        adj[u].append(v)
        adj[v].append(u)  # undirected

    visited = [0] * V
    components = []

    def dfs(node, singleComponent):
        visited[node] = 1
        singleComponent.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor, singleComponent)

    # Traverse all vertices
    for i in range(V):
        if not visited[i]:
            singleComponent = []
            dfs(i, singleComponent)
            singleComponent.sort()          # sort in increasing order
            components.append(singleComponent)

    return components
