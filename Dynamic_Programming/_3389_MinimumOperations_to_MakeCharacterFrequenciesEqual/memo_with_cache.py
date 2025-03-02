from functools import cache
from collections import Counter

class Solution:
    def makeStringGood(self, s: str) -> int:
        freq = Counter(s)
        max_freq = max(freq.values(), default=0)

        @cache
        def dfs(i, expectedOcc, leftoverChars):
            # Base case: If all 26 characters have been processed
            if i == 26:
                return 0

            char = chr(i + ord('a'))
            occurance = freq.get(char, 0)

            # Case 1: Character not in the string
            if occurance == 0:
                return dfs(i + 1, expectedOcc, 0)

            # Case 2: Frequency is greater than expected
            if occurance > expectedOcc:
                return occurance - expectedOcc + dfs(i + 1, expectedOcc, occurance - expectedOcc)

            # Case 3: Frequency is less than expected
            if occurance + leftoverChars < expectedOcc:
                return min(
                    expectedOcc - occurance - leftoverChars + dfs(i + 1, expectedOcc, 0),
                    occurance + dfs(i + 1, expectedOcc, occurance)
                )

            # Case 4: Frequency matches expected or can be balanced
            return dfs(i + 1, expectedOcc, 0)

        min_cost = float('inf')
        for expectedOcc in range(max_freq + 1):
            min_cost = min(min_cost, dfs(0, expectedOcc, 0))

        return min_cost

