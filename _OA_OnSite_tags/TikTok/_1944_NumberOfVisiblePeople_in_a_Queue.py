from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        stk = []

        for i in range(n):
            while stk and heights[stk[-1]] < heights[i]:
                res[stk.pop()] += 1

            if stk:
                res[stk[-1]] += 1

            stk.append(i)

        return res