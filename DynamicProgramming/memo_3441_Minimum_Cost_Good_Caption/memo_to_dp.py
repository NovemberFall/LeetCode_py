class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return -1

        s = [ord(c) - ord('a') for c in caption]
        f = [[0] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(26):
                if i + 5 < n:
                    cost1 = f[i + 1][j] + abs(s[i] - j)
                    cost2 = min(f[i + 3])
