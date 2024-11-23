from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        a = nums[0] * nums[1] * nums[n - 1]
        b = nums[n - 1] * nums[n - 2] * nums[n - 3]
        return max(a, b)


