from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def dfs(i):
            if i <= 1:
                return 0
            return min(dfs(i - 1) + cost[i - 1], dfs(i - 2) + cost[i - 2])
        return dfs(n)

