from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                dp[i] |= dp[j]
        return dp[0]