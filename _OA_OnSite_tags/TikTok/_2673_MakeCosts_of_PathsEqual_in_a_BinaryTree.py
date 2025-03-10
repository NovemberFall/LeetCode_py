from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        increment = 0
        def dfs(index):
            nonlocal increment
            if index > len(cost):
                return 0
            left_cost = dfs(index * 2)
            right_cost = dfs(index * 2 + 1)
            increment += abs(right_cost - left_cost)
            return max(left_cost, right_cost) + cost[index - 1]

        dfs(1)
        return increment