from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        n = len(nums)
        dp = [-1] * n
        return self.f(nums, dp, k, 0)

    def f(self, nums: List[int], dp: List[int], k: int, index) -> int:
        if index >= len(nums):
            return 0
        if index <= len(nums) -1 and k == 0 :
            dp[index] = max(dp)
            return dp[index]

        pick = dp[index] + self.f(nums, dp, k - 1, index + 2)
        notPick = self.f(nums, dp, k - 1, index + 1)
        return max(notPick, pick)
