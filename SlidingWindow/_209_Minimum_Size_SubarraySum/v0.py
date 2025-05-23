from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = float('inf')
        curr_sum = 0
        left = 0
        for right, x in enumerate(nums):
            curr_sum += x
            while curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return res if res != float('inf') else 0