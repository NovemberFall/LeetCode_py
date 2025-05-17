from functools import cache

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007

        @cache
        def dfs(i) -> int:
            if i < 0:
                return 0
            if i == 0:
                return 1
            return (dfs(i - zero) + dfs(i - one)) % MOD
        return sum(dfs(length) for length in range(low, high + 1)) % MOD