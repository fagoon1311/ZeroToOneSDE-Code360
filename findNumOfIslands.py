# Problem Statement: Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands. Note: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.


# Approach: We can solve this problem using BFS or DFS. We will use BFS here. We will traverse the grid and whenever we find a land, we will start BFS from that land and mark all the connected lands as visited
'''
Time Complexity: O(n * m)
Space Complexity: O(n * m)

'''

from collections import deque


def bfs(row, col, vis, grid, directions):
  vis[row][col] = 1
  q = deque()
  q.append((row, col))

  while q:
    currx, curry = q.popleft()

    for dx, dy in directions:
      newX = currx + dx
      newY = curry + dy

      if newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]) and vis[newX][newY] == 0 and grid[newX][newY] == 1:
        vis[newX][newY] = 1
        q.append((newX, newY))



def findIslands(mat, n, m):
  vis = [[0] * m for _ in range(n)]
  count = 0
  directions = [(-1,-1), (-1, 0), (-1, 1), (0,1), (1, 1), (1, 0), (1, -1), (0, -1)]
  for i in range(n):
    for j in range(m):
      if vis[i][j] != 1 and mat[i][j] == 1:
        count += 1
        bfs(i, j, vis, mat, directions)

  return count
