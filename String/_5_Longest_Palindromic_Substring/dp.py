class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        res = ""

        # base case: single char
        for i in range(n):
            dp[i][i] = True
            res = s[i]   # at least 1 char

        # fill table
        for length in range(2, n + 1):  # substring length
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r]:
                    if length == 2 or dp[l + 1][r - 1]:
                        dp[l][r] = True
                        if length > len(res):
                            res = s[l:r + 1]

        return res