from functools import cache


class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return -1

        s = []
        for c in caption:
            s.append(ord(c) - ord('a'))

        @cache
        def dfs(i, j):
            if i == n:
                return 0

            if i + 5 < n:
                # Option 1: Skip forming a good caption, just convert current char to match j
                cost1 = abs(s[i] - j) + dfs(i + 1, j)

                # Option 2: Form a good caption with 3 chars at i, i+1, i+2
                min_next = float('inf')
                for k in range(26):
                    min_next = min(min_next, dfs(i + 3, k))

                cost_block_3 = abs(s[i] - j) + abs(s[i + 1] - j) + abs(s[i + 2] - j)
                cost2 = cost_block_3 + min_next
                return min(cost1, cost2)
            else:
                # Not enough space to form a "good caption", so just do option 1
                return abs(s[i] - j) + dfs(i + 1, j)


        res = float('inf')
        for j in range(26):
            res = min(res, dfs(0, j))
        return res



