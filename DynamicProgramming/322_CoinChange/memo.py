from functools import cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(remaining: int) -> int:
            if remaining < 0:
                return -1
            if remaining == 0:
                return 0

            min_count = float('inf')
            for coin in coins:
                res = dfs(remaining - coin)
                if res >= 0:
                    min_count = min(min_count, res + 1)

            return -1 if min_count == float('inf') else min_count

        return dfs(amount)
