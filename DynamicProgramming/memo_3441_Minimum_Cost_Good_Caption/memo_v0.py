# 只计算最Code 小操作次数的代码 (that only calculates the minimum number of operations)
import functools # Import necessary for @cache (though often @functools.cache is used)
from functools import cache # More direct import

class Solution:
    def minCostGoodCaption(self, caption: str) -> int:
        n = len(caption)

        # If the string length is less than 3, it's impossible
        if n < 3:
            return -1

        # 2. Preprocessing:
        # Example: "cat" becomes [2, 0, 19]
        s = [ord(c) - ord('a') for c in caption]

        @cache
        def dfs(i: int, j: int) -> int:
            if i == n:
                return 0

            res = dfs(i + 1, j) + abs(s[i] - j)

            if i <= n - 6:
                cost_block_3 = abs(s[i] - j) + abs(s[i + 1] - j) + abs(s[i + 2] - j)

                min_cost_remaining = min(dfs(i + 3, k) for k in range(26))

                cost_option_b = cost_block_3 + min_cost_remaining

                res = min(res, cost_option_b)

            return res

        return min(dfs(0, j) for j in range(26))