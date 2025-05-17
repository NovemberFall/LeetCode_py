from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(index):
            if index < 0:
                return 0
            res = max(dfs(index - 1), nums[index] + dfs(index - 2))
            return res

        return dfs(n - 1)
