from collections import deque
# Implement Flood fill alogorithm

# Solution 1 - DFS
'''
Time Complexity: O(n * m)
Space Complexity: O(n * m) 

'''

def dfs(r, c, image, directions, inicolor, newColor):
  m = len(image)
  n = len(image[0])

  image[r][c] = newColor

  for d in directions:
      newR, newC = r + d[0], c + d[1]

      if newR >= 0 and newR < m and newC >= 0 and newC < n and image[newR][newC] == inicolor and image[newR][newC] != newColor:
          dfs(newR, newC, image, directions, inicolor, newColor)


def floodFill(image, x, y, newColor):
  # Write your Code here.
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

  inicolor = image[x][y]

  dfs(x, y, image, directions, inicolor, newColor)

  return image

# Solution 2 - BFS


def floodFill2(image, x, y, newColor):
    m, n = len(image), len(image[0])
    inicolor = image[x][y]

    if inicolor == newColor:
        return image  # No need to fill

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque()
    queue.append((x, y))

    while queue:
        r, c = queue.popleft()

        # Only fill if it matches the initial color
        if image[r][c] == inicolor:
            image[r][c] = newColor

            for dr, dc in directions:
                newR, newC = r + dr, c + dc

                if 0 <= newR < m and 0 <= newC < n and image[newR][newC] == inicolor:
                    queue.append((newR, newC))

    return image
