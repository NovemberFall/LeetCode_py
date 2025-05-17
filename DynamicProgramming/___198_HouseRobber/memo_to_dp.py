
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 2)
        for index, num in enumerate(nums):
            f[index + 2] = max(f[index + 1], f[index] + num)
        return f[n + 1]