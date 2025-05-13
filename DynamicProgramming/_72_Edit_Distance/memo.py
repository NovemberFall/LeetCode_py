class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1 = word1
        self.word2 = word2
        m, n = len(word1), len(word2)
        # dp[i][j] will store the minimum edit distance between word1[i:] and word2[j:]
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.dfs(dp, m, n, 0, 0)

    # i: current index in word1, j: current index in word2
    def dfs(self, dp, m, n, i, j):
        # Base case 1: If word1 is exhausted, insert remaining characters from word2
        if i == m:
            return n - j
        # Base case 2: If word2 is exhausted, delete remaining characters from word1
        if j == n:
            return m - i

        if dp[i][j] != -1:
            return dp[i][j]

        # If current characters match, no operation needed, move to the next pair
        if self.word1[i] == self.word2[j]:
            dp[i][j] = self.dfs(dp, m, n, i + 1, j + 1)
        else:
            # If characters don't match, consider three operations:
            # Insert: Insert char from word2 into word1 (match word1[i] with word2[j+1:])
            insert = 1 + self.dfs(dp, m, n, i, j + 1)
            # Delete: Delete char from word1 (match word1[i+1:] with word2[j:])
            delete = 1 + self.dfs(dp, m, n, i + 1, j)
            # Replace: Replace char in word1 with char from word2 (match word1[i+1:] with word2[j+1:])
            replace = 1 + self.dfs(dp, m, n, i + 1, j + 1)
            dp[i][j] = min(insert, delete, replace)
        return dp[i][j]

