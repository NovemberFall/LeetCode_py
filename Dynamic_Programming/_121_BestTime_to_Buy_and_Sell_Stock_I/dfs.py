class Solution:
    def helper(self, prices, i, n, buy, k, dp):
        if i == n:
            return 0  # Base case: no more days left
        if k == 0:
            return 0  # Base case: no more transactions allowed

        if dp[i][buy][k] != -1:
            return dp[i][buy][k]

        if buy == 0:
            # Case when we can either buy or skip buying today
            dont_take = self.helper(prices, i + 1, n, 0, k, dp)  # Skip buying
            take = -prices[i] + self.helper(prices, i + 1, n, 1, k - 1, dp)  # Buy today
        else:
            # Case when we can either sell or skip selling today
            dont_take = self.helper(prices, i + 1, n, 1, k, dp)  # Skip selling
            take = prices[i] + self.helper(prices, i + 1, n, 0, k - 1, dp)  # Sell today

        dp[i][buy][k] = max(take, dont_take)
        return dp[i][buy][k]

    def maxProfit(self, prices):
        n = len(prices)
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]  # 3D dp table for i, buy, k
        return self.helper(prices, 0, n, 0, 2, dp)
