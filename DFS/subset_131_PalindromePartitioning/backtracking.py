from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        path = []

        # consider how to split s[i:]
        def dfs(i) -> None:
            if i == n:
                res.append(path.copy())
                return

            for j in range(i, n):
                substr = s[i:j + 1]
                if substr == substr[::-1]:
                    path.append(substr)
                    # 考虑剩余的 s[j+1:] 怎么分割
                    dfs(j + 1)
                    path.pop()
        dfs(0)
        return res
