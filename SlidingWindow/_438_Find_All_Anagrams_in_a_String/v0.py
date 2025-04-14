class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        if len(p) > len(s):
            return res

        # Record the frequency of characters in p
        p_freq = [0] * 26
        for ch in p:
            p_freq[ord(ch) - ord('a')] += 1

        window = [0] * 26
        slow = 0
        for fast in range(len(s)):
            window[ord(s[fast]) - ord('a')] += 1

            if fast - slow + 1 == len(p):
                if window == p_freq:
                    res.append(slow)
                window[ord(s[slow]) - ord('a')] -= 1
                slow += 1

        return res
