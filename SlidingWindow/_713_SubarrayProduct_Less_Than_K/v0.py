from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        res = 0
        product = 1
        left = 0
        for right, num in enumerate(nums):
            product *= num
            while product >= k:
                product //= nums[left]
                left += 1
            res += right - left + 1
        return res

