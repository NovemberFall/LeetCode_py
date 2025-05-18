from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            res = 0
            for num in nums:
                if i >= num:
                    res += dp[i - num]
            dp[i] = res
        return dp[target]