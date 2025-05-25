from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)

        def backtracking(i):
            res.append(path.copy())

            for j in range(i, n):
                path.append(nums[j])
                backtracking(j + 1)
                path.pop()
        backtracking(0)
        return res
