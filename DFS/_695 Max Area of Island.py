from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(grid, i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            return (dfs(grid, i + 1, j)
                    + dfs(grid, i, j + 1)
                    + dfs(grid, i - 1, j)
                    + dfs(grid, i, j - 1) + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(grid, i, j))

        return res
