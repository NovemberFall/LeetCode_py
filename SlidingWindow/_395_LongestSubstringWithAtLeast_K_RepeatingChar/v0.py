class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maxUniqueChars = self.getCountOfUniqueChars(s)
        freq = [0] * 26
        res = 0
        for targetUnique in range(1, maxUniqueChars + 1):
            freq = [0] * 26
            window_unique_count, numCharsWithFreqAtLeastK, left, right = 0, 0, 0, 0
            while right < len(s):
                if window_unique_count <= targetUnique:
                    idx = ord(s[right]) - ord('a')
                    if freq[idx] == 0:
                        window_unique_count += 1
                    freq[idx] += 1
                    if freq[idx] == k:
                        numCharsWithFreqAtLeastK += 1
                    right += 1
                else:
                    idx = ord(s[left]) - ord('a')
                    if freq[idx] == k:
                        numCharsWithFreqAtLeastK -= 1
                    freq[idx] -= 1
                    if freq[idx] == 0:
                        window_unique_count -= 1
                    left += 1

                if window_unique_count == numCharsWithFreqAtLeastK:
                    res = max(res, right - left)
        return res

    def getCountOfUniqueChars(self, s):
        uniqueChars = [False] * 26
        uniqueNums = 0
        for char in s:
            idx = ord(char) - ord('a')
            if not uniqueChars[idx]:
                uniqueNums += 1
                uniqueChars[idx] = True
        return uniqueNums