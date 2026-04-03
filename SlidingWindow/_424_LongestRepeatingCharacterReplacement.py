from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = Counter()
        res = 0
        max_freq = 0
        left = 0

        for right, c in enumerate(s):
            # expand
            cnt[c] += 1
            max_freq = max(max_freq, cnt[c])

            # shrink (⚠️ condition changed)
            while (right - left + 1) - max_freq > k:
                cnt[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res