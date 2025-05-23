from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0] * 2 for _ in range(3)]

        dp[0][1] = -float('inf')
        dp[1][1] = -prices[0]
        dp[2][1] = -float('inf')


        for i in range(1, n):
            dp[1][1] = max(dp[1][1], - prices[i])
            dp[1][0] = max(dp[1][0], dp[1][1] + prices[i])

            dp[2][1] = max(dp[2][1], dp[1][0] - prices[i])
            dp[2][0] = max(dp[2][0], dp[2][1] + prices[i])
        return max(dp[1][0], dp[2][0])