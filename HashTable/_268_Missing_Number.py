from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        arr = set(nums)
        for missing in range(0, n + 1):
            if missing not in arr:
                return missing
        return -1