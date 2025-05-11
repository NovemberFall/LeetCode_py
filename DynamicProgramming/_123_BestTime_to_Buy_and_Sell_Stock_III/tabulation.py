from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(2 + 1)] for _ in range(2)] for _ in range(n + 1)]
        for index in range(n - 1, -1, -1):
            for is_buy in range(2):
                for transactions_left in range(1, 3):
                    if is_buy:
                        dp[index][is_buy][transactions_left] = (
                            max(-prices[index] + dp[index + 1][0][transactions_left], 0 + dp[index + 1][1][transactions_left]))
                    else:
                        dp[index][is_buy][transactions_left] = (
                            max(prices[index] + dp[index + 1][1][transactions_left - 1], 0 + dp[index + 1][0][transactions_left]))

        return dp[0][1][2]
