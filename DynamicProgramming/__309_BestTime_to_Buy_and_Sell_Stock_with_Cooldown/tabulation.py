from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        dp = [[0] * 3 for _ in range(n + 1)]
        dp[0][0] = -float('inf')
        dp[0][1] = -prices[0]
        dp[0][2] = -float('inf')

        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i - 1])
            dp[i][2] = dp[i - 1][1] + prices[i - 1]

        return dp[n][2]
