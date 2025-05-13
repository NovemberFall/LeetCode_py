from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        dp1 = [-1] * n
        dp2 = [-1] * n

        return max(self.f(nums, dp1, 0, n - 2), self.f(nums, dp2, 1, n - 1))

    def f(self, nums, dp, index, end):
        if index > end:
            return 0
        if index == end:
            return nums[index]
        if dp[index] != -1:
            return dp[index]

        pick = self.f(nums, dp, index + 2, end) + nums[index]
        notPick = self.f(nums, dp, index + 1, end)

        dp[index] = max(pick, notPick)
        return dp[index]