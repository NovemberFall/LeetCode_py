from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_cnt = Counter()          # current window character count
        t_cnt = Counter(p)         # target frequency (pattern p)
        k = len(p)                 # fixed window size (length of p)

        left = 0                   # left pointer of sliding window
        res = []                  # store starting indices of valid anagrams

        for right, c in enumerate(s):
            # 1. expand window: include current character
            s_cnt[c] += 1

            # 2. shrink window if size exceeds k
            # keep window size always == k
            if right - left + 1 > k:
                s_cnt[s[left]] -= 1   # remove leftmost character
                left += 1             # move left pointer forward

            # 3. check if current window matches target
            # condition:
            #   - same size (k)
            #   - same frequency map → anagram
            if s_cnt == t_cnt and (right - left + 1) == k:
                res.append(left)      # record starting index

        return res