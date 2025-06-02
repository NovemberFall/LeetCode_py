from functools import cache
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        @cache
        def dfs(index) -> int:
            res = 1
            for j in range(index):
                if nums[j] < nums[index]:
                    res = max(res, dfs(j) + 1)
            return res

        return max(dfs(i) for i in range(len(nums)))