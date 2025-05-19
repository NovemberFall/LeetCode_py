from functools import cache


class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        # A valid "good caption" must be at least length 3
        if n < 3:
            return -1

        # Preprocessing:
        # Convert each character to its corresponding index in the alphabet
        # Example: "cat" becomes [2, 0, 19]
        s = [ord(c) - ord('a') for c in caption]

        @cache
        def dfs(i, j):
            # Base case: if we reach the end of the string, no cost needed
            if i == n:
                return 0

            # If we still have at least 6 characters left,
            # we can try to create a block of 3 same letters (good caption)
            if i <= n - 6:
                # Option 1: Just change the current character to match `j` and move on
                cost1 = abs(s[i] - j) + dfs(i + 1, j)

                # Option 2: Force a "good caption" block starting at i (length 3)
                # All three characters must match `j`, so calculate cost to convert them
                cost_block_3 = abs(s[i] - j) + abs(s[i + 1] - j) + abs(s[i + 2] - j)

                # Then recursively solve the rest starting at position i + 3
                # Try all possible characters for the next block and pick the minimum cost
                min_next = float('inf')
                for k in range(26):
                    min_next = min(min_next, dfs(i + 3, k))

                cost2 = cost_block_3 + min_next
                return min(cost1, cost2)
            else:
                # Not enough space to form a "good caption", so just do option 1
                return abs(s[i] - j) + dfs(i + 1, j)

        res = float('inf')
        for j in range(26):
            res = min(res, dfs(0, j))
        return res
