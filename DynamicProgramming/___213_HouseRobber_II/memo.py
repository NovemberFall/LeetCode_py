from functools import cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        @cache
        def dfs(i, end) -> int:
            if i > end:
                return 0
            return max(dfs(i + 1, end), dfs(i + 2, end) + nums[i])
        return max(dfs(0, n - 2), dfs(1, n - 1))
