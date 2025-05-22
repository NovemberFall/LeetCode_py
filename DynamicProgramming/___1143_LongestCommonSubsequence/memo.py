class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.t1 = text1
        self.t2 = text2
        m, n = len(text1), len(text2)
        self.dp = [[-1] * (n + 1) for _ in range(m + 1)]
        return self.dfs(0, 0)

    def dfs(self, i, j):
        # Base case: If we have reached the end of either string, the LCS length is 0
        if i == len(self.t1) or j == len(self.t2):
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        if self.t1[i] == self.t2[j]:
            # Include the current character and move to the next in both strings
            self.dp[i][j] = 1 + self.dfs(i + 1, j + 1)
        else:
            # If characters don't match, explore two possibilities:
            # 1. Skip character in text1 (move to i+1)
            # 2. Skip character in text2 (move to j+1)
            # Take the maximum of these two possibilities
            self.dp[i][j] = max(self.dfs(i + 1, j), self.dfs(i, j + 1))

        return self.dp[i][j]

