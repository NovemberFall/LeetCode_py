from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        if len(arr) == 0 or k == 0:
            return res
        close = self.binary_search(arr, x)
        res.append(arr[close])
        left = close - 1
        right = close + 1
        while len(res) < k:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= len(arr):
                res.append(arr[left])
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
        return sorted(res)


    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left < right - 1:
            mid = (left + right) >> 1
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid
            else:
                right = mid

        if abs(arr[left] - target) <= abs(arr[right] - target):
            return left
        else:
            return right


