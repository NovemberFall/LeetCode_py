from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True
        for i in range(n - 2, -1, -1):
            dp[i] = any(dp[i + 1: min(i + nums[i] + 1, n)])
        return dp[0]