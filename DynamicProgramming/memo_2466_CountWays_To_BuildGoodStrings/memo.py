from functools import cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007

        @cache
        def countWays(length) -> int:
            if length < 0:
                return 0  # Invalid string length
            if length == 0:
                return 1  # One valid way: empty string

            # Total ways = build string ending with `zero` zeros + `one` ones
            ways_from_zero = countWays(length - zero)
            ways_from_one = countWays(length - one)

            total_ways = (ways_from_zero + ways_from_one) % MOD
            return total_ways

        total = 0
        for length in range(low, high + 1):
            total = (total + countWays(length)) % MOD
        return total
