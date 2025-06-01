from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_count = Counter()
        t_count = Counter(t)

        res_left, res_right = -1, len(s)
        left = 0
        for right, c in enumerate(s):
            s_count[c] += 1
            while s_count >= t_count:
                if right - left + 1 < res_right - res_left + 1:
                    res_left, res_right = left, right
                s_count[s[left]] -= 1
                left += 1
        return "" if res_left < 0 else s[res_left: res_right + 1]