from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # since for num[i] from value 1 to target, the length is target
        length = target
        dp = [[0] * (length + 1) for _ in range(target + 1)]
        dp[0][0] = 1