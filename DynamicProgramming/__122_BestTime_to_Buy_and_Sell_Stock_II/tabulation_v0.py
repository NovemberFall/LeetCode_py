from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(len(prices) + 1)]
        for index in range(n - 1, -1, -1):
            for is_buy in range(2):
                if is_buy:
                    buy = -prices[index] + dp[index + 1][0]
                    skip = 0 + dp[index + 1][1]
                    dp[index][is_buy] = max(buy, skip)
                else:
                    sell = prices[index] + dp[index + 1][1]
                    hold = 0 + dp[index + 1][0]
                    dp[index][is_buy] = max(sell, hold)

        return dp[0][1]