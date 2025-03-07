from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # Edge case optimization: If k is large enough, this problem reduces to Leetcode 122
        # if k >= n // 2:
        #     return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

        dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(n + 1)]
        for index in range(n - 1, -1, -1):
            for is_buy in range(2):
                for t_l in range(1, k + 1):
                    if is_buy:
                        dp[index][is_buy][t_l] = max(-prices[index] + dp[index + 1][0][t_l], dp[index + 1][1][t_l])
                    else:
                        dp[index][is_buy][t_l] = max(prices[index] + dp[index + 1][1][t_l - 1], dp[index + 1][0][t_l])

        return dp[0][1][k]