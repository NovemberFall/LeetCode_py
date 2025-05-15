from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        # dp[i][0]: cash on hand at the end of day i, not holding stock
        # dp[i][1]: cash on hand at the end of day i, holding stock

        dp[0][0] = 0 # dp[0][0]: Before considering any prices, not holding -> cash is 0.
        # dp[0][1]: Before considering any prices, holding -> This state is impossible.
        dp[0][1] = -float('inf')

        # Iterate through the prices, considering 1 price up to n prices
        # dp[i] will store the results after considering the first 'i' prices (prices[0]...prices[i-1])
        for i in range(1, n + 1):
            # Max of:
            # 1. Not holding after i-1 prices (dp[i-1][0]) and skipped the current price.
            # 2. Holding after i-1 prices (dp[i-1][1]) and sold the current price (+ prices[i-1]).
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            # Max of:
            # 1. Holding after i-1 prices (dp[i-1][1]) and held the current price.
            # 2. Negative of the current price (-prices[i-1]). (This term appears to represent buying today, setting cash to -price).
            dp[i][1] = max(dp[i - 1][1], -prices[i - 1])

        # The final answer is the maximum cash after considering all 'n' prices (dp[n]),
        # when not holding stock (state 0), as profit is realized upon selling.
        return dp[n][0]
