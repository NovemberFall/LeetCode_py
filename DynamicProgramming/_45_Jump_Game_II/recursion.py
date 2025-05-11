from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.dfs(nums, 0)

    def dfs(self, nums: List[int], index: int) -> int:
        if index == len(nums) - 1:
            return 0

        min_jumps = float('inf')
        i = index + 1
        while i <= (index + nums[index]) and i < len(nums):
            min_jumps = min(min_jumps, self.dfs(nums, i) + 1)
            i += 1
        return min_jumps
