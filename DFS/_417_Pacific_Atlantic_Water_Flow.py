from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[False for _ in range(n)] for _ in range(m)]
        for col in range(n):
            self.dfs(0, col, heights, heights[0][col], pacific)
            self.dfs(m - 1, col, heights, heights[m - 1][col], atlantic)
        for row in range(m):
            self.dfs(row, 0, heights, heights[row][0], pacific)
            self.dfs(row, n - 1, heights, heights[row][n - 1], atlantic)

        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    cell = []
                    cell.append(i)
                    cell.append(j)
                    res.append(cell)
        return res

    def dfs(self, i, j, heights, prev, ocean) -> None:
        if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]) or heights[i][j] < prev \
                or ocean[i][j]:
            return

        ocean[i][j] = True

        self.dfs(i - 1, j, heights, heights[i][j], ocean)
        self.dfs(i, j - 1, heights, heights[i][j], ocean)
        self.dfs(i + 1, j, heights, heights[i][j], ocean)
        self.dfs(i, j + 1, heights, heights[i][j], ocean)
