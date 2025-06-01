from typing import List

class twoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i
        return
