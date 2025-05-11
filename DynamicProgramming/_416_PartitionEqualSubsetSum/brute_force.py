from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return self.dfs(nums, subset_sum, n)

    def dfs(self, nums: List[int], subset_sum: int, n: int) -> bool:
        if subset_sum == 0:
            return True
        if n == 0:
            return False
        if subset_sum < 0:
            return False

        res = (self.dfs(nums, subset_sum - nums[n - 1], n - 1) or
               self.dfs(nums, subset_sum, n - 1) )
        return res