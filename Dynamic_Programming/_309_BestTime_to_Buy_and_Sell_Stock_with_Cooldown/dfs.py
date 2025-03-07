from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.dfs(prices, True, 0)

    def dfs(self, prices, is_buy, index):
        # Base case: If we've processed all days, no profit can be made
        if index >= len(prices):
            return 0

        if is_buy:
            # Option 1: Buy the stock today
            buy = - prices[index] + self.dfs(prices, False, index + 1)
            # Option 2: Do not buy today
            skip = 0 + self.dfs(prices, True, index + 1)
            # Return the maximum profit between buying and skipping
            return max(buy, skip)
        else:
            # Option 1: Sell the stock today (after a cooldown)
            sell = prices[index] + self.dfs(prices, True, index + 2)
            # Option 2: Do not sell today
            hold = 0 + self.dfs(prices, False, index + 1)
            # Return the maximum profit between selling and holding
            return max(sell, hold)