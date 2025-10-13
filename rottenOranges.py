from collections import deque
# You have been given a grid containing some oranges. Each cell of this grid has one of the three integers values:

# Value 0 - representing an empty cell.
# Value 1 - representing a fresh orange.
# Value 2 - representing a rotten orange.
# Every second, any fresh orange that is adjacent(4-directionally) to a rotten orange becomes rotten.

# Your task is to find out the minimum time after which no cell has a fresh orange. If it's impossible to rot all the fresh oranges then print -1.


'''
Time Complexity: O(n * m)
Space Complexity: O(n * m)

'''

def rottenOranges(grid, n, m):
  q = deque()
  time = 0
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

  # Collect all the rotten oranges in the queue
  for i in range(n):
      for j in range(m):
          if grid[i][j] == 2:
              q.append((i, j))

  # BFS
  while q:
    currSize = len(q)
    rottenThisRound = False

    while currSize > 0:
        currx, curry = q.popleft()

        for x, y in directions:
          newx, newy = x + currx, y + curry
          if 0 <= newx < n and 0 <= newy < m and grid[newx][newy] == 1:
              grid[newx][newy] = 2
              q.append((newx, newy))
              rottenThisRound = True
        currSize -= 1

    if rottenThisRound:
        time += 1


  # Check if there are any fresh oranges left
  for i in range(n):
      for j in range(m):
          if grid[i][j] == 1:
              return -1
  return time
        
  