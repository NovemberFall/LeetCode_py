from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0

        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][1] = -float('inf')

        for i in range(1, n + 1):
            dp[i & 1][1] = max(dp[(i - 1) & 1][1], dp[(i - 1) & 1][0] - prices[i - 1])
            dp[i & 1][0] = max(dp[(i - 1) & 1][0], dp[i & 1][1] + prices[i - 1] - fee)
        return dp[n & 1][0]
