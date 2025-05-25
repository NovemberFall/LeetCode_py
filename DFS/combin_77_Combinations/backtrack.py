from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(index, k):
            if k == 0:
                res.append(path.copy())
                return

            for j in range(index, n + 1):
                path.append(j)
                backtrack(j + 1, k - 1)
                path.pop()

        backtrack(1, k)
        return res



