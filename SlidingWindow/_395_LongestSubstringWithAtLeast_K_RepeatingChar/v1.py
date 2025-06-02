class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        total_unique_chras = len(set(s))
        res = 0
        for cur_uni_char in range(1, total_unique_chras + 1):
            freq = [0] * 26
            left, right = 0, 0
            window_unique_chars = 0
            chars_atleast_k = 0
            while right < len(s):
                if window_unique_chars <= cur_uni_char:
                    index = ord(s[right]) - ord('a')
                    if freq[index] == 0:
                        window_unique_chars += 1
                    freq[index] += 1
                    if freq[index] == k:
                        chars_atleast_k += 1
                    right += 1
                else:
                    index = ord(s[left]) - ord('a')
                    if freq[index] == k:
                        chars_atleast_k -= 1
                    freq[index] -= 1
                    if freq[index] == 0:
                        window_unique_chars -= 1
                    left += 1

                if window_unique_chars == chars_atleast_k:
                    res = max(res, right - left)
        return res
