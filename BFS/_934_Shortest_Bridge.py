from collections import deque
from typing import List


class Solution:
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        firstX, firstY = -1, -1
        # Find any land cell (value 1) to start DFS
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    firstX, firstY = i, j
                    break
            # If firstX is NOT -1 (meaning a cell was found in the current row)
            # break the outer loop as well.
            if firstX != -1:
                break

        # Initialize BFS queue
        bfs_queue = deque()

        # Find all cells of the first island using DFS and add to queue
        # Marks island cells as 2
        self.dfs(grid, firstX, firstY, n, bfs_queue)

        distance = 0  # init Bridge length
        # start BFS from the first island:
        while bfs_queue:
            level_size = len(bfs_queue)  # Cells at current distance
            # Process cells at the current distance level
            for _ in range(level_size):
                cur_cell = bfs_queue.popleft()
                x, y = cur_cell[0], cur_cell[1]

                # Explore neighbors
                for dx, dy in self.dirs:
                    nextX, nextY = x + dx, y + dy
                    # check bounds:
                    if 0 <= nextX < n and 0 <= nextY < n:
                        # If neighbor is land of the second island (value 1)
                        if grid[nextX][nextY] == 1:
                            return distance  # Found the bridge
                        # If neighbor is unvisited water (value 0)
                        elif grid[nextX][nextY] == 0:
                            # Mark water as visited (-1) and add to queue for next level
                            grid[nextX][nextY] = -1
                            bfs_queue.append((nextX, nextY))
                        # Skip visited cells (2 or -1)
                    # Else: Neighbor is out of bounds, skip

            # Increment distance after processing a level
            distance += 1

        # should not be reached in valid cases with two islands
        return -1

    def dfs(self, grid, x, y, n, bfs_queue):
        # Mark current cell as visited (part of island 1)
        grid[x][y] = 2
        # Add cell to BFS queue
        bfs_queue.append((x, y))

        # Explore neighbors
        for dx, dy in self.dirs:
            curX, curY = x + dx, y + dy
            # Check bounds and if neighbor is unvisited land (value 1)
            if 0 <= curX < n and 0 <= curY < n and grid[curX][curY] == 1:
                self.dfs(grid, curX, curY, n, bfs_queue)
