from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # Shortcut: If k is large enough, the shortest path is just Manhattan distance
        # because we can eliminate any obstacle on the direct path (m-1 + n-1 steps).
        if k >= m + n - 2:
            return m + n - 2

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]
        visited[0][0][k] = True

        # Queue: (row, col, steps taken, remaining k)
        queue = deque([(0, 0, 0, k)])

        while queue:
            size = len(queue)
            for i in range(size):
                row, col, steps, kLeft = queue.popleft()

                # Reached the goal
                if row == m - 1 and col == n - 1:
                    return steps

                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc

                    # Check boundaries
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    nextK = kLeft - grid[nr][nc]
                    if nextK >= 0 and not visited[nr][nc][nextK]:
                        visited[nr][nc][nextK] = True
                        queue.append((nr, nc, steps + 1, nextK))
        return -1 # No path found
