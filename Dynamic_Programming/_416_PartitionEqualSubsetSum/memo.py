from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        sub_sum = total_sum // 2
        memo = {}
        n = len(nums)
        return self.dfs(sub_sum, nums, memo, n)

    def dfs(self, sub_sum, nums, memo, n) -> bool:
        if sub_sum == 0:
            return True
        if n == 0:
            return False
        if sub_sum < 0:
            return False

        if (n, sub_sum) in memo:
            return memo[(n, sub_sum)]

        res = (self.dfs(sub_sum - nums[n - 1], nums, memo, n - 1) or
               self.dfs(sub_sum, nums, memo, n - 1))
        memo[(n, sub_sum)] = res
        return res
