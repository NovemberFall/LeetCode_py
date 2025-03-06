from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.dfs(prices, True, 0)

    def dfs(self, prices: List[int], is_buy, index):
        if index == len(prices):
            return 0

        if is_buy:
            return max(self.dfs(prices, False, index + 1) - prices[index],
                       0 + self.dfs(prices, True, index + 1))

