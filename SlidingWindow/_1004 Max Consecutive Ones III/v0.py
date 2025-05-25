from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        flip_zero_to_one = 0
        left = 0
        for right, x in enumerate(nums):
            if x == 0:
                flip_zero_to_one += 1
            while flip_zero_to_one > k:
                if nums[left] == 0:
                    flip_zero_to_one -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
