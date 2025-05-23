class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # EMPTY s1,s2 can surely interleave to form EMPTY s3

        for i in range(1, m + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i - 1][0]

        for j in range(1, n + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s3[i + j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i - 1][j]
                elif s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = False
        return dp[m][n]

