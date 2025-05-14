from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # 第 2 维的 0 没有意义，1 表示交易进行了 1 次，2 表示交易进行了 2 次
        # 为了使得第 2 维的数值 1 和 2 有意义，这里将第 2 维的长度设置为 3
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]

        dp[0][1][0] = 0
        # 第 3 维规定了必须持股，因此是 -prices[0]
        dp[0][1][1] = -prices[0]

        dp[0][1][0] = 0
        # 还没发生的交易，持股的时候应该初始化为负无穷
        dp[0][2][1] = -float('inf')

        for i in range(1, n):
            # 转移顺序先持股，再卖出
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][1][0] - prices[i])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])

            dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i])
            dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i])

        return max
