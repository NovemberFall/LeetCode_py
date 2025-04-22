from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(n + 1)]
        for index in range(n - 1, -1, -1):
            for buy in range(2):
                for t_l in range(1, 2):
                    if buy:
                        dp[index][buy][t_l] = max(-prices[index] + dp[index + 1][0][t_l], dp[index + 1][1][t_l])
                    else:
                        dp[index][buy][t_l] = max(prices[index] + dp[index + 1][1][t_l - 1], dp[index + 1][0][t_l])

        return dp[0][1][1]
