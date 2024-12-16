from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ls, rs = nums[0], nums[r]
        count = 0
        while l < r:
            if ls == rs:
                l += 1
                r -= 1
                ls = nums[l]
                rs = nums[r]
            elif ls < rs:
                count += 1
                l += 1
                ls += nums[l]
            elif ls > rs:
                count += 1
                r -= 1
                rs += nums[r]

        return count

