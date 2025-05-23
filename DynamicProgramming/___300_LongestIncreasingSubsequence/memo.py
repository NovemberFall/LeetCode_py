from functools import cache
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        @cache
        def dfs(index) -> int:
            res = 0
            for j in range(index):
                if nums[j] < nums[index]:
                    res = max(res, dfs(j))
            return res + 1

        return max(dfs(i) for i in range(len(nums)))
