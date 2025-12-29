'''

✔ What is Kruskal’s Algorithm?

Greedy algorithm to find MST.

Picks edges in increasing weight order.

Ensures no cycle is formed.

✔ Why use DSU (Disjoint Set Union)?

Quickly checks if two nodes belong to the same component.

Prevents cycles.

Uses find + union operations.

✔ DSU Optimizations Used

Path Compression: Speeds up find() by flattening the tree.

Union by Rank: Attaches smaller tree under larger one to keep structure balanced.

✔ Steps in Kruskal’s Algorithm

Sort all edges by weight (ascending).

Initialize DSU where each node is its own parent.

For each smallest edge:

If endpoints have different parents → add to MST.

Perform union operation.

Stop after choosing n − 1 edges.

✔ Why Kruskal Works? (Cut Property)

Lightest edge crossing any cut is always safe to include in MST.

✔ Time Complexity

Sorting edges: O(m log m)

DSU operations: Almost O(1)

Total: O(m log m)

✔ When is Kruskal best?

When edges are fewer or the graph is sparse.

Works even on disconnected graphs to find Minimum Spanning Forest.

'''





from typing import List
class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]

    def findUP(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findUP(self.parent[node])

        return self.parent[node]


    def unionByRank(self, u, v):
        ulp_u, ulp_v = self.findUP(u), self.findUP(v)
        if ulp_u == ulp_v:
            return 

        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v

        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u

        else:
            self.parent[ulp_u] = ulp_v
            self.rank[ulp_v] += 1


def kruskalMST(n: int, edges: List[List[int]]) -> int:
    # Write your code here
    ds = DisjointSet(n)
    ans = 0
    edges.sort(key = lambda x: x[2])
    for u, v, w in edges:
        if ds.findUP(u) != ds.findUP(v):
            ans += w
            ds.unionByRank(u, v)

    return ans