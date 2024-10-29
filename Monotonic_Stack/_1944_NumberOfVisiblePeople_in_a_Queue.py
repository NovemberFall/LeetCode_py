from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        if heights is None or n == 0:
            return []

        ans = [0] * n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and heights[i] > heights[stk[-1]]:
                stk.pop()
                ans[i] += 1
            if stk:
                ans[i] += 1
            stk.append(i)

        return ans