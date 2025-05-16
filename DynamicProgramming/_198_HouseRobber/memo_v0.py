from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        return self.f(nums, dp, 0)

    def f(self, nums: List[int], dp: List[int], index: int) -> int:
        if index == len(nums) - 1:
            return nums[index]

        if index >= len(nums):
            return 0

        if dp[index] != -1:
            return dp[index]

        pick = nums[index] + self.f(nums, dp, index + 2)
        notPick = self.f(nums, dp, index + 1)
        dp[index] = max(pick, notPick)
        return dp[index]
