import math
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        res = math.inf
        while left <= right:
            mid = (left + right) // 2
            if self.canShip(mid, weights, days):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res

    def canShip(self, mid: int, weights: List[int], days: int) -> bool:
        ships = 1
        curCap = mid
        for w in weights:
            if curCap < w:
                ships += 1
                curCap = mid
            curCap -= w
        return ships <= days
