from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        path = []
        def dfs(index, target):
            if target == 0:
                res.append(path.copy())
                return

            if target - candidates[index] < 0:
                return

            for j in range(index, n):
                path.append(candidates[j])
                dfs(j, target - candidates[j])
                path.pop()
        dfs(0, target)
        return res
