from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n + 2)]
        for index in range(n - 1, -1, -1):
            for is_buy in range(2):
                if is_buy:
                    dp[index][is_buy] = max(-prices[index] + dp[index + 1][0], dp[index + 1][1])
                else:
                    dp[index][is_buy] = max(prices[index] + dp[index + 2][1], dp[index + 1][0])

        return dp[0][1]