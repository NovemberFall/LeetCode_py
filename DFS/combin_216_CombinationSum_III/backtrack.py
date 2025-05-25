from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        cur_sum = n

        def backtrack(index, remaining):
            if len(path) == k and remaining == 0:
                res.append(path.copy())
                return

            if remaining < 0:
                return

            for j in range(index, min(9 + 1, n + 1)):
                path.append(j)
                backtrack(j + 1, remaining - j)
                path.pop()

        backtrack(1, cur_sum)
        return res



