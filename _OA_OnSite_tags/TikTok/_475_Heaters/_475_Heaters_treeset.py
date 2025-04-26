from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heater_set = []
        res = 0

        for h in houses:
            heater_set.add(h)

        for house in houses:
            upper = min(heater_set, key=lambda x: x if x >= house else None)
            lower = max(heater_set, key=lambda x: x if x <= house else None)

            d1 = upper - house if upper else float('inf')
            d2 = house - lower if lower else float('inf')

            res = max(res, min(d1, d2))

        return res

