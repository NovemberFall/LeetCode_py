from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        res[0] = self.findFirst(nums, target)
        res[1] = self.findLast(nums, target)
        return res

    def findFirst(self, nums: List[int], target: int) -> int:
        idx = -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                idx = mid;
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return idx

    def findLast(self, nums: List[int], target: int) -> int:
        idx = -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                idx = mid;
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return idx