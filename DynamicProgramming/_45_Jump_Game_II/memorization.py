from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        return self.dfs(nums, dp, 0)

    def dfs(self, nums: List[int], dp: List[int], index: int) -> int:
        if index == len(nums) - 1:
            dp[index] = 0
            return dp[index]

        if dp[index] != -1:
            return dp[index]

        min_jumps = float("inf")
        i = index + 1
        while i <= (index + nums[index]) and i < len(nums):
            min_jumps = min(min_jumps, self.dfs(nums, dp, i) + 1)
            i += 1
        dp[index] = min_jumps
        return dp[index]


