class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0] = list(range(n + 1))  # 递归边界 f[0][j] = j
        for i in range(1, m + 1):
            dp[i][0] = i  # 递归边界

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:  # 最短公共超序列一定包含 str1[i]
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:  # 取更短的组成答案
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        res = []
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i - 1][j] + 1:
                res.append(str1[i - 1])
                i -= 1
            else:
                res.append(str2[j - 1])
                j -= 1
        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        while j > 0:
            res.append(str2[j - 1])
            j -= 1

        return "".join(reversed(res))
