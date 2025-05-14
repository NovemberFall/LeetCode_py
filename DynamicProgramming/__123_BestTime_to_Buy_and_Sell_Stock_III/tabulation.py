from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i][k][holding_status]
        # i: Day index (0 to n-1)
        # k: Number of transactions completed (1 or 2 represent meaningful values)
        # holding_status: 0 (not holding stock), 1 (holding stock)
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]

        # 第 3 维规定了必须持股，因此是 -prices[0]
        dp[0][1][1] = -prices[0]  # Represents buying on day 0, ending day 0 holding.
        dp[0][1][0] = 0  # Day 0, 1 transaction completed, not holding stock.

        # Day 0, 2 transactions completed, holding stock
        dp[0][2][1] = -float('inf')  # Day 0, 2 transactions completed, not holding stock. (Impossible state)
        dp[0][2][0] = -float('inf')  # This state should also typically be -infinity initially

        for i in range(1, n):
            # 转移顺序先持股，再卖出
            # --- Transitions for k = 1 completed transaction ---
            # Max of:
            # 1. Held from day i-1 (dp[i-1][1][1]), staying at 1 completed.
            # 2. Bought today (-prices[i]), coming from a state where you were not holding
            dp[i][1][1] = max(dp[i - 1][1][1], - prices[i])
            # Max of:
            # 1. Was not holding day i-1 (dp[i-1][1][0]), staying at 1 completed.
            # 2. Sold today (+ prices[i]), from holding state (dp[i-1][1][1]). Selling completes a transaction, moving to 2 completed.
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])

            # --- Transitions for k = 2 completed transactions ---
            # Max of:
            # 1. Held from day i-1 (dp[i-1][2][1]), staying at 2 completed.
            # 2. Bought today (-prices[i]), coming from not holding state with 1 completed (dp[i-1][1][0]).
            dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i])
            # Max of:
            # 1. Was not holding day i-1 (dp[i-1][2][0]), staying at 2 completed.
            # 2. Sold today (+ prices[i]), from holding state with 2 completed (dp[i-1][2][1]).
            dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i])

        # The final answer is the maximum cash at the end of the last day (index n-1),
        # when not holding stock, with either 1 completed transaction (dp[n-1][1][0]) or 2 completed transactions (dp[n-1][2][0]).
        # This covers the cases where the maximum profit is achieved after completing 1 or 2 transactions.
        return max(dp[n - 1][1][0], dp[n - 1][2][0])
