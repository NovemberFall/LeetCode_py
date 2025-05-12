class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1 = word1
        self.word2 = word2
        m, n = len(word1), len(word2)
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.dfs(dp, m, n, 0, 0)

    def dfs(self, dp, m, n, i, j):
        if i == m:
            return n - j
        if j == n:
            return m - i

        if dp[i][j] != -1:
            return dp[i][j]

        if self.word1[i] == self.word2[j]:
            dp[i][j] = self.dfs(dp, m, n, i + 1, j + 1)
        else:
            insert = 1 + self.dfs(dp, m, n, i, j + 1)
            delete = 1 + self.dfs(dp, m, n, i + 1, j)
            replace = 1 + self.dfs(dp, m, n, i + 1, j + 1)
            dp[i][j] = min(insert, delete, replace)
        return dp[i][j]

