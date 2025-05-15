from typing import List
import math # Import math for -math.inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        # states:
        # 0: Not holding stock, not in cooldown (can buy today)
        # 1: Holding stock (can sell today)
        # 2: Just sold stock (in cooldown today, cannot buy)
        dp = [[0] * 3 for _ in range(n + 1)]

        # dp[0][0]: Before day 0, not holding, not in cooldown -> profit is 0. Correct.
        dp[0][0] = 0
        # dp[0][1]: Before day 0, holding -> impossible. Initialize with -inf.
        dp[0][1] = -math.inf
        # dp[0][2]: Before day 0, just sold -> impossible. Initialize with -inf.
        dp[0][2] = -math.inf

        # The price on the current day (index i-1) is prices[i-1].
        # The loop already goes from 1 to n+1 (exclusive end), meaning i will be 1, 2, ..., n.
        for i in range(1, n + 1):

            # Calculate dp[i][0] (Max profit after considering first i prices, not holding, not in cooldown)
            # We could reach this state by:
            # 1. Being in state 0 yesterday (dp[i-1][0]) and skipping price i-1.
            # 2. Being in state 2 yesterday (dp[i-1][2]) - finished cooldown on day i-2, so today (day i-1) we are free to buy.
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])

            # Calculate dp[i][1] (Max profit after considering first i prices, holding stock)
            # We could reach this state by:
            # 1. Being in state 1 yesterday (dp[i-1][1]) and holding price i-1.
            # 2. Being in state 0 yesterday (dp[i-1][0]) and buying price i-1 (- prices[i-1]).
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i - 1]) # Corrected transition

            # Calculate dp[i][2] (Max profit after considering first i prices, just sold stock)
            # We could reach this state by:
            # 1. Must have been holding yesterday (dp[i-1][1]) and sold price i-1 (+ prices[i-1]).
            dp[i][2] = dp[i - 1][1] + prices[i - 1]

        # The maximum profit can end in state 0 (not holding, not in cooldown - meaning we finished all transactions and cooldowns)
        # or in state 2 (just sold - meaning the last action was a sell). It cannot end in state 1 (holding) for realized profit.
        return max(dp[n][0], dp[n][2]) # Correct final result
