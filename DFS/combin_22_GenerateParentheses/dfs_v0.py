from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def dfs(left, right):
            if left == right == n:
                res.append("".join(path))
                return

            if left < n:
                path.append('(')
                dfs(left + 1, right)
                path.pop()
            if right < left:
                path.append(')')
                dfs(left, right + 1)
                path.pop()

        dfs(0, 0)
        return res