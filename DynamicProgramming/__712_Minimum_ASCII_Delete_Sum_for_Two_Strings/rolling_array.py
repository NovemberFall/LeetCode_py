class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            dp[i % 2][0] = dp[(i - 1) % 2][0] + ord(s1[i - 1])
            for j in range(1, n + 1):
                if s1[(i - 1)] == s2[j - 1]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
                else:
                    dp[i % 2][j] = min(dp[(i - 1) % 2][j] + ord(s1[i - 1]), dp[i % 2][j - 1] + ord(s2[j - 1]))
        return dp[m % 2][n]
