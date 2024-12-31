from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        distinct_islands = set()
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    path = []
                    self.dfs(grid, i, j, path, 'o')
                    distinct_islands.add("".join(path))
        return len(distinct_islands)

    def dfs(self, grid: List[List[int]], i: int, j: int, path: [], dir: str) -> None:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return

        path.append(dir)
        grid[i][j] = 0

        self.dfs(grid, i + 1, j, path, 'u')
        self.dfs(grid, i - 1, j, path, 'd')
        self.dfs(grid, i, j - 1, path, 'l')
        self.dfs(grid, i, j + 1, path, 'r')

        path.append('b')
