from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (left + right) >> 1
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        if nums[left] < nums[right]:
            return right
        else:
            return left