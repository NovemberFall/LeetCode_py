# 只计算最小操作次数的代码 (Code that only calculates the minimum number of operations)
import functools # Import necessary for @cache (though often @functools.cache is used)
from functools import cache # More direct import

class Solution:
    def minCostGoodCaption(self, s: str) -> int:
        n = len(s) # Get the length of the input string

        # 1. Basic Constraint Check:
        # If the string length is less than 3, it's impossible to form even one
        # block of length 3. The problem likely defines this as impossible,
        # hence returning -1.
        if n < 3:
            return -1

        # 2. Preprocessing:
        # Convert the string characters 'a' through 'z' into integers 0 through 25.
        # This makes calculating the cost (absolute difference) easier.
        # Example: "cat" becomes [2, 0, 19]
        s = [ord(c) - ord('a') for c in s]

        # 3. Memoized Recursive Function (Dynamic Programming):
        # @cache is a decorator (from functools) that automatically memoizes
        # the results of the dfs function. If dfs(i, j) is called with the
        # same arguments multiple times, the stored result is returned instantly,
        # avoiding redundant computations. This turns the recursion into DP.
        @cache
        def dfs(i: int, j: int) -> int:
            """
            Calculates the minimum cost to make the suffix s[i:] a valid "good caption",
            assuming the character at index i MUST be part of a block of character j (0-25).

            Args:
                i: The starting index of the substring we are currently considering.
                j: The target character (as an integer 0-25) for the block that includes index i.

            Returns:
                The minimum cost for the suffix s[i:].
            """

            # 4. Base Case for Recursion:
            # If the index `i` reaches the end of the string (`n`), we have successfully
            # processed the entire string according to the rules. The cost for an
            # empty suffix is 0.
            if i == n:
                return 0

            # 5. Recursive Transitions (Calculating the cost for state (i, j)):

            # Option A: Extend the current block of character 'j'.
            # Cost = (cost to change s[i] to j) + (min cost for the rest of the string s[i+1:],
            #                                       assuming s[i+1] also becomes j)
            # This allows forming blocks of length 4, 5, 6, ... by repeatedly choosing this option.
            res = dfs(i + 1, j) + abs(s[i] - j)

            # Option B: Finish the current block at s[i+2] (forming a block of length >= 3)
            #           and start a *new* block from s[i+3].
            # This option is only possible if we have enough characters remaining
            # to form a block of 3 starting at `i` (i, i+1, i+2) AND potentially
            # form another block of at least 3 starting at `i+3` (i+3, i+4, i+5).
            # The condition `i <= n - 6` ensures that index `i+5` is valid (i.e., `i+5 < n`).
            if i <= n - 6:
                # Cost of forming the block of 3 'j's starting at i:
                cost_block_3 = abs(s[i] - j) + abs(s[i + 1] - j) + abs(s[i + 2] - j)

                # Find the minimum cost for the remaining suffix s[i+3:]
                # The next block (starting at i+3) can be *any* character k (0-25).
                # We need to find the minimum cost among all possible next block characters.
                min_cost_remaining = min(dfs(i + 3, k) for k in range(26))

                # Total cost for Option B = (cost of current block of 3) + (min cost for the rest)
                cost_option_b = cost_block_3 + min_cost_remaining

                # Choose the minimum cost between Option A and Option B.
                res = min(res, cost_option_b)

            # Return the calculated minimum cost for this state (i, j)
            return res

        # 6. Initial Call:
        # The very first block (starting at index 0) can consist of any character 'j' (0-25).
        # We need to calculate the minimum cost for each possible starting character
        # and take the overall minimum.
        # `dfs(0, j)` calculates the min cost assuming the string starts with a block of 'j'.
        return min(dfs(0, j) for j in range(26))