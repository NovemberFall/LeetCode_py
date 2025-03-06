from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.dfs(prices, True, 0)

    def dfs(self, prices, is_buy, index):
        if index >= len(prices):
            return 0

        if is_buy:
            buy = - prices[index] + self.dfs(prices, False, index + 1)
            skip = 0 + self.dfs(prices, True, index + 1)
            return max(buy, skip)
        else:
            sell = prices[index] + self.dfs(prices, True, index + 2)
                       0 + self.dfs(prices, False, index + 1))
