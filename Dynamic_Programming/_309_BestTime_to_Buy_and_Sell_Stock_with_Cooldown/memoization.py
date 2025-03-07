from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1 for _ in range(2)] for row in range(len(prices))]

        def dfs(is_buy, index) -> int:
            if index >= len(prices):
                return 0
            if dp[index][is_buy] != -1:
                return dp[index][is_buy]

            if is_buy:
                buy = -prices[index] + dfs(0, index + 1)
                skip = 0 + dfs(1, index + 1)
                dp[index][is_buy] = max(skip, buy)
                return dp[index][is_buy]
            else:
                sell = prices[index] + dfs(1, index + 2)
                hold = 0 + dfs(0, index + 1)
                dp[index][is_buy] = max(sell, hold)
                return dp[index][is_buy]

        return dfs(1, 0)