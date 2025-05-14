from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]

        # dp[i][0]: cash on hand at the end of day i, not holding stock
        # dp[i][1]: cash on hand at the end of day i, holding stock

        # Set the base case values for day 0 (index 0)
        dp[0][0] = 0 # not holding stock at end of day 0 -> cash is 0
        dp[0][1] = -prices[0] # holding stock at end of day 0 -> cash is -price of day 0 (bought on day 0)

        for i in range(1, n):
            # Calculate dp[i][0]: Cash at the end of day i, not holding stock
            # Max of:
            # 1. Cash from end of day i-1, not holding (dp[i-1][0]), and skipped transaction today.
            # 2. Cash from end of day i-1, holding (dp[i-1][1]), and sold stock today (+ prices[i]).
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])

            # Calculate dp[i][1]: Cash at the end of day i, holding stock
            # Max of:
            # 1. Cash from end of day i-1, holding (dp[i-1][1]), and held stock today.
            # 2. Negative of today's price (-prices[i]). (You bought a stock on day i. To do this, you must have not been holding a stock at the end of day i-1).
            dp[i][1] = max(dp[i - 1][1], -prices[i])
            # You were already holding a stock at the end of day i-1 (dp[i - 1][1]),
            # and you continued to hold it on day i. Your cash remains dp[i - 1][1].

        # The final answer is the cash on hand at the end of the last day (index n-1),
        # when not holding stock (dp[n-1][0]), as profit is realized upon selling.
        return dp[n - 1][0]
