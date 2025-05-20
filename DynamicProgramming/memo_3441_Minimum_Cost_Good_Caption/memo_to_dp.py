class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return -1

        s = [ord(c) - ord('a') for c in caption]
        f = [[0] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(26):
                cost1 = f[i + 1][j] + abs(s[i] - j)
                cost2 = float('inf')
                if i <= n - 6:
                    cost2 = min(abs(s[i] - j) + abs(s[i + 1] - j), abs(s[i + 2] - j) + f[i + 3])

                f[i][j] = min(cost1, cost2)
        return min(f[0])



