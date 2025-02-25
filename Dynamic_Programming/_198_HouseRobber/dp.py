from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            notPick = dp[i - 1]
            pick = dp[i - 2] + nums[i]
            dp[i] = max(pick, notPick)
        return dp[len(nums) - 1]
