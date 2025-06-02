from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        distinct_islands = set()

        def dfs(grid, i, j, path, dir):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            path.append(dir)
            grid[i][j] = 0
            dfs(grid, i - 1, j, path, 'u')
            dfs(grid, i + 1, j, path, 'd')
            dfs(grid, i, j - 1, path, 'l')
            dfs(grid, i, j + 1, path, 'r')
            path.append('back')

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    dfs(grid, i, j, path, '')
                    distinct_islands.add("".join(path))

        return len(distinct_islands)
