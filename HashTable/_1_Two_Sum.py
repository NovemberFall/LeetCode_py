from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, num in enumerate(nums):
            if target - num in map:
                return [map[target - num], index]
            map[num] = index
        return [-1, -1]