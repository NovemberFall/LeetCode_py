from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()  # in place
        first, last = strs[0], strs[len(strs) - 1]
        idx = 0

        while idx < len(first) and idx < len(last):
            if first[idx] == last[idx]:
                idx += 1
            else:
                break

        return first[0: idx]