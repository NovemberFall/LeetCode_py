from typing import List


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        # rows, cols = len(values), len(values[0])
        all_items = [num for row in values for num in row]

        all_items.sort()

        return sum((day + 1) * price for day, price in enumerate(all_items))