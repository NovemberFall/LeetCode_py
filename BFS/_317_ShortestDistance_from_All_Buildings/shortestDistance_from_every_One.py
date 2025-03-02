from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        minDistance = float('inf')
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])

        distances = [[[0] * 2 for _ in range(cols)] for _ in range(rows)]
        buildings = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    buildings += 1
                    self.bfs(grid, distances, i, j)

        for i in range(rows):
            for j in range(cols):
                if distances[i][j][1] == buildings:
                    minDistance = min(minDistance, distances[i][j][0])

        return -1 if minDistance == float('inf') else minDistance

    def bfs(self, grid, distances, i, j):
        rows, cols = len(grid), len(grid[0])
        queue = deque([(i, j)])

        visited = [[False] * cols for _ in range(rows)]
        visited[i][j] = True

        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()
                # If we reached an empty cell, then add the distance and increment the count of houses reached at this cell.
                if grid[row][col] == 0:
                    distances[row][col][0] += steps
                    distances[row][col][1] += 1

                # Traverse the next cells which is not a blockage.
                for dir in self.dirs:
                    nextRow, nextCol = row + dir[0], col + dir[1]
                    if nextRow < 0 or nextRow >= rows or nextCol < 0 or nextCol >= cols or visited[nextRow][nextCol]:
                        continue
                    if grid[nextRow][nextCol] == 0:
                        visited[nextRow][nextCol] = True
                        queue.append((nextRow, nextCol))
            steps += 1


