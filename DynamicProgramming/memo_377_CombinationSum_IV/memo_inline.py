from functools import cache
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i) -> int:
            if i == 0:
                return 1
            return sum(dfs(i - num) for num in nums if num <= i)
        return dfs(target)

