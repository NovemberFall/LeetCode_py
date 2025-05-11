from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(len(prices))]
        return self.dfs(prices, 1, dp, 0)

    def dfs(self, prices, is_buy, dp, index) -> int:
        if index >= len(prices):
            return 0
        if dp[index][is_buy] != -1:
            return dp[index][is_buy]

        if is_buy:
            buy = -prices[index] + self.dfs(prices, 0, dp, index + 1)
            skip = self.dfs(prices, 1, dp, index + 1)
            dp[index][is_buy] = max(buy, skip)
            return dp[index][is_buy]
        else:
            sell = prices[index] + self.dfs(prices, 1, dp, index + 1)
            hold = self.dfs(prices, 0, dp, index + 1)
            dp[index][is_buy] = max(sell, hold)
            return dp[index][is_buy]