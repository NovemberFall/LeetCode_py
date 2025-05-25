from typing import List


MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res = []
        if digits is None or len(digits) == 0:
            return res
        path = [''] * n
        def dfs(index) -> None:
            if index == n:
                res.append("".join(path))
                return

            for c in MAPPING[int(digits[index])]:
                path[index] = c
                dfs(index + 1)
        dfs(0)
        return res
