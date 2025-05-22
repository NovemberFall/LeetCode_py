class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            dp[i % 2][0] = i  # base case: transforming word1[0:i] to empty word2
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
                else:
                    insert = dp[i % 2][j - 1] + 1
                    delete = dp[(i - 1) % 2][j] + 1
                    replace = dp[(i - 1) % 2][j - 1] + 1
                    dp[i % 2][j] = min(insert, delete, replace)
        return dp[m % 2][n]
