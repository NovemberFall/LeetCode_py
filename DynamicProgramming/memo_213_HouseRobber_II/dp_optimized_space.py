from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0] + self.f(nums[2:-1]), self.f(nums[1:]))

    def f(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for num in nums:
            new_f = max(f1, f0 + num)
            f0 = f1
            f1 = new_f
        return f1