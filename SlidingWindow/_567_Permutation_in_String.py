from charset_normalizer.cd import Counter
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s_cnt = Counter()           # sliding window frequency
        t_cnt = Counter(s1)         # target frequency (pattern)
        k = len(s1)                 # fixed window size

        left = 0
        for right, c in enumerate(s2):
            # 1. expand window: include current character
            s_cnt[c] += 1

            # 2. keep window size == k
            if right - left + 1 > k:
                s_cnt[s2[left]] -= 1

                # 🔥 remove key if count becomes 0 (important!)
                if s_cnt[s2[left]] == 0:
                    del s_cnt[s2[left]]

                left += 1

            # 3. check if current window is a permutation of s1
            if right - left + 1 == k and s_cnt == t_cnt:
                return True

        return False