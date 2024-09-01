from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = length - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            self.reverse(nums, 0)
            return

        j = length - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1

        self.swap(nums, i, j)
        self.reverse(nums, i + 1)

    def reverse(self, nums: List[int], i: int) -> None:
        left, right = i, len(nums) - 1
        while left <= right:
            self.swap(nums, left, right)
            left += 1
            right -= 1

    def swap(self, nums, left, right) -> None:
        nums[left], nums[right] = nums[right], nums[left]
