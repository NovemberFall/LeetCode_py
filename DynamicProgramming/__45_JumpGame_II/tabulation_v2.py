from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[n - 1] = 0
        for i in range(n - 2, -1, -1):
            # Try all jumps from i to i + nums[i]
            dp[i] = 1 + min(dp[i + 1: min(i + nums[i] + 1, n)], default=float('inf'))
        return dp[0]
