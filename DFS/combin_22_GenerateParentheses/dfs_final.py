from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(res, [], n, 0, 0)
        return res

    def dfs(self, res: List[str], path: List[str], n: int, left: int, right: int) -> None:
        if left == n and right == n:
            res.append("".join(path))
            return
        if right > left:
            return

        if left < n:
            path.append('(')
            self.dfs(res, path, n, left + 1, right)
            path.pop()
        if right < n:
            path.append(')')
            self.dfs(res, path, n, left, right + 1)
            path.pop()
