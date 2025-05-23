from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        k = 2

        # dp[i][k][holding_status]
        # i: Day index (0 to n-1)
        # k: Number of transactions completed (1 or 2 represent meaningful values)
        # holding_status: 0 (not holding stock), 1 (holding stock)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]

        dp[0][0][1] = -float('inf')  # invalid state: holding with 0 transactions
        dp[0][1][1] = -prices[0]  # buy stock on day 0, using 1 transaction
        dp[0][2][1] = -float('inf')  # can't complete 2 transactions on day 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Update holding status:
                # Option 1: do nothing, still holding from yesterday
                # Option 2: buy today (only if not holding yesterday and have one less transaction)
                dp[i & 1][j][1] = max(dp[(i - 1) & 1][j][1], dp[(i - 1) & 1][j - 1][0] - prices[i - 1])
                # Update not holding status:
                # Option 1: do nothing, still not holding
                # Option 2: sell today (must have held yesterday)
                dp[i & 1][j][0] = max(dp[(i - 1) & 1][j][0], dp[(i - 1) & 1][j][1] + prices[i - 1])
        # Return the max profit at the end, after 2 transactions, not holding stock
        return dp[n & 1][2][0]