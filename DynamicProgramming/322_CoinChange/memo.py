from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None] * (amount + 1)
        return self.dfs(coins, dp, amount)

    def dfs(self, coins: List[int], dp: List[int], amount: int) -> int:
        if amount < 0:
            return -1

        if amount == 0:
            return 0

        if dp[amount] is not None:
            return dp[amount]

        min_count = float('inf')
        for coin in coins:
            res = self.dfs(coins, dp, amount - coin)
            if res == -1:
                continue
            min_count = min(min_count, 1 + res)
        dp[amount] = -1 if min_count == float('inf') else min_count
        return dp[amount]
