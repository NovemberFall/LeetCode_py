from typing import List

class Solution:
    def __init__(self):
        self.map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits is None or len(digits) == 0:
            return res

        self.dfs(res, digits, [], 0)
        return res


    def dfs(self, res: [], digits: str, path: list[str], index: int):
        if index == len(digits):
            res.append("".join(path))
            return

        cur = self.map[int(digits[index])]
        for char in cur:
            path.append(char)
            self.dfs(res, digits, path, index + 1)
            path.pop()
