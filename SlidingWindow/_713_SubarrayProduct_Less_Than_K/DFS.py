from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        self.res = 0

        for i in range(len(nums)):
            self.dfs(nums, i, 1, k)
        return self.res

    def dfs(self, nums, index, cur_product, k):
        if index == len(nums):
            return

        cur_product *= nums[index]

        if cur_product < k:
            self.res += 1
            # continue expanding
            self.dfs(nums, index + 1, cur_product, k)
        else:
            # stop early (important pruning)
            return
