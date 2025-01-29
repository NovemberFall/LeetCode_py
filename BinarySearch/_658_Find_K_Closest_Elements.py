from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 0 or k == 0:
            return []

        # Find the closest element
        close = self.closest(arr, x)

        # Initialize pointers around the closest element
        left = close - 1
        right = close + 1

        # Expand the window to include `k` elements
        while right - left - 1 < k:  # Ensure window size is `k`
            if left < 0:  # If no more elements on the left, move right
                right += 1
            elif right >= len(arr):  # If no more elements on the right, move left
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):  # Compare distances
                left -= 1
            else:
                right += 1

        # Return the subarray of size `k`
        return arr[left + 1:right]

    def closest(self, arr, target):
        left, right = 0, len(arr) - 1
        if right < 0:
            return -1

        # Binary search to find the closest element
        while left < right - 1:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid
            else:
                right = mid

        # Determine the closer of the two candidates
        if abs(arr[left] - target) <= abs(arr[right] - target):
            return left
        return right



