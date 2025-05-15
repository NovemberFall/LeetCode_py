from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k == 0 or n < 2:
            return 0
        if k >= n // 2:
            return self.greedy(prices)

        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]

        for j in range(0, k + 1):
            dp[0][j][1] = -float('inf')

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
        return dp[n][k][0]

    def greedy(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res