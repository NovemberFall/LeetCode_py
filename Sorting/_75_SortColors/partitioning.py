import random
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero = 0
        two = n
        i = 0
        while i < two:
            if nums[i] == 0:
                self.swap(nums, i, zero)
                zero += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                two -= 1
                self.swap(nums, i, two)


    def swap(self, nums: List[int], left: int, right: int) -> None:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
