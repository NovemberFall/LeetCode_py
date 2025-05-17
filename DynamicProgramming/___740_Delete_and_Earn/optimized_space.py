from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        count = [0] * (max_num + 1)
        for x in nums:
            count[x] += x  # accumulate points for number x

        # start DP => Rolling Array operations to calculate the final result:
        f0 = f1 = 0
        for num in count:
            new_f = max(f1, f0 + num)
            f0 = f1
            f1 = new_f
        return f1