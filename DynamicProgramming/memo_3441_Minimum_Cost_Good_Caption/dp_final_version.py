from math import inf
from string import ascii_lowercase


class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""

        s = [ord(c) - ord('a') for c in caption]
        f = [[0] * 26 for _ in range(n + 1)]
        min_j = [0] * (n + 1)
        next = [[0] * 26 for _ in range(n + 1)]  # 用一个 nxt 数组记录每个状态 f[i][j] 的最优决策来自哪
        for i in range(n - 1, -1, -1):
            mn = float('inf')
            for j in range(26):
                res = f[i + 1][j] + abs(s[i] - j)
                res2 = f[i + 3][min_j[i + 3]] + abs(s[i] - j) + abs(s[i + 1] - j) + abs(s[i + 2] - j) if i <= n - 6 else inf
                if res2 < res or res2 == res and min_j[i + 3] < j:
                    res = res2
                    next[i][j] = min_j[i + 3]  # 记录转移来源
                else:
                    next[i][j] = j  # 记录转移来源

                f[i][j] = res
                if res < mn:
                    mn = res
                    min_j[i] = j  # 记录最小的 f[i][j] 中的 j 是多少

        ans = [''] * n
        i = 0
        j = min_j[0]
        while i < n:
            ans[i] = ascii_lowercase[j]
            # print(ascii_lowercase[j])
            k = next[i][j]
            if k == j:
                i += 1
            else:
                ans[i + 2] = ans[i + 1] = ans[i]
                i += 3
                j = k
        return ''.join(ans)

