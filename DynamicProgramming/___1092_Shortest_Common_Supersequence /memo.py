from functools import cache


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        @cache
        def dfs(i, j):
            if i < 0:
                return str2[:j+1]
            if j < 0:
                return str1[:i+1]
            if str1[i] == str2[j]:  # 最短公共超序列一定包含 s[i]
                return dfs(i-1, j-1) + str1[i]
            pick_str1 = dfs(i - 1, j) + str1[i]
            pick_str2 = dfs(i, j - 1) + str2[j]
            if len(pick_str1) < len(pick_str2):
                return pick_str1
            else:
                return pick_str2

        return dfs(m - 1, n - 1)
