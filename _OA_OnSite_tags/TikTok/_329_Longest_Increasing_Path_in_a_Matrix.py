from typing import List


class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.dirs = [[0, 1],[0, -1],[1, 0],[-1, 0]]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix) == 0:
            return 0
        self.m = len(matrix)
        self.n = len(matrix[0])
        longest = 0
        memo = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                longest = max(longest, self.dfs(matrix, i, j, memo))
        return longest

    def dfs(self, matrix, i, j, memo) -> int:
        if memo[i][j] != 0:
            return memo[i][j]

        maxLen = 1
        for dir in self.dirs:
            row = i + dir[0]
            col = j + dir[1]
            if row >= 0 and row < self.m and col >= 0 and col < self.n and matrix[row][col] > matrix[i][j]:
                maxLen = max(maxLen, 1 + self.dfs(matrix, row, col, memo))

        memo[i][j] = maxLen
        return maxLen

