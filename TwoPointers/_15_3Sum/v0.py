from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for first in range(0, len(nums) - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            second = first + 1
            third = len(nums) - 1
            while second < third:
                cur_sum = nums[first] + nums[second] + nums[third]
                if cur_sum == 0:
                    res.add((nums[first], nums[second], nums[third]))
                elif cur_sum > 0:
                    third -= 1
                else:
                    second += 1
        return [list(triple) for triple in res]