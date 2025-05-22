from functools import cache
from math import inf
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return inf

            if i == 0 and j == 0:
                return grid[i][j]

            return min(dfs(i - 1, j), dfs(i, j - 1)) + grid[i][j]

        return dfs(m - 1, n - 1)
