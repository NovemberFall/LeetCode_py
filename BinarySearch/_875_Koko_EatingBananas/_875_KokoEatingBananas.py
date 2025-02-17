from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = self.getMaxPile(piles)
        while left < right:
            mid = (left + right) >> 1
            if self.canEatAllBananas(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return right

    def getMaxPile(self, piles):
        max_pile = float('-inf')
        for pile in piles:
            max_pile = max(max_pile, pile)
        return max_pile

    def canEatAllBananas(self, piles, speed, H):
        hours = 0
        for pile in piles:
            hours += pile // speed
            if pile % speed == 0:
                hours += 1
        return hours <= H
