class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        self.s = s
        self.p = p
        dp = [[None for _ in range(n + 1)] for _ in range(m + 1)]
        return self.dfs(dp,0, 0)

    def dfs(self, dp, i, j):
        if j == len(self.p):
            dp[i][j] = (i == len(self.s))
            return dp[i][j]

        if dp[i][j] is not None:
            return dp[i][j]


        if j + 1 < len(self.p) and self.p[j + 1] == '*':
            if i < len(self.s) and (self.p[j] == '.' or self.s[i] == self.p[j]):
                if self.dfs(dp, i + 1, j):
                    dp[i][j] = True
                    return dp[i][j]
            if self.dfs(dp, i, j + 2):
                dp[i][j] = True
                return dp[i][j]

            dp[i][j] = False
            return dp[i][j]
        else:
            if i < len(self.s) and (self.p[j] == '.' or self.s[i] == self.p[j]):
                dp[i][j] = self.dfs(dp, i + 1, j + 1)
                return dp[i][j]
            dp[i][j] = False
            return dp[i][j]




