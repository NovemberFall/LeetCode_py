from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # Initialize a 3D DP array with -1
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        return self.dfs(prices, 1, 2, dp, 0)

    def dfs(self, prices, is_buy, transactions_left, dp, index) -> int:
        if index >= len(prices) or transactions_left == 0:
            return 0
        # if transactions_left == 0:
        #     return 0
        if dp[index][is_buy][transactions_left] != -1:
            return dp[index][is_buy][transactions_left]

        if is_buy:
            buy = -prices[index] + self.dfs(prices, 0, transactions_left, dp, index + 1)
            skip = self.dfs(prices, 1, transactions_left, dp, index + 1)
            dp[index][is_buy][transactions_left] = max(buy, skip)
        else:
            sell = prices[index] + self.dfs(prices, 1, transactions_left - 1, dp, index + 1)
            hold = self.dfs(prices, 0, transactions_left, dp, index + 1)
            dp[index][is_buy][transactions_left] = max(sell, hold)

        return dp[index][is_buy][transactions_left]