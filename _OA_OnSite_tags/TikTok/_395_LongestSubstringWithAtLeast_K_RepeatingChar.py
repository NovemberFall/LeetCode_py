class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maxUniqueChars = self.getCountOfUniqueChars(s)
        freq = [0] * 26
        res = 0
        for curUniqueChars in range(1, maxUniqueChars + 1):
            freq = [0] * 26
            uniqueChars, countOfUniqueCharsAtLeastK, slow, fast = 0, 0, 0, 0
            while fast < len(s):
                if uniqueChars <= curUniqueChars:
                    idx = ord(s[fast]) - ord('a')
                    if freq[idx] == 0:
                        uniqueChars += 1
                    freq[idx] += 1
                    if freq[idx] == k:
                        countOfUniqueCharsAtLeastK += 1
                    fast += 1
                else:
                    idx = ord(s[slow]) - ord('a')
                    if freq[idx] == k:
                        countOfUniqueCharsAtLeastK -= 1
                    freq[idx] -= 1
                    if freq[idx] == 0:
                        uniqueChars -= 1
                    slow += 1

                if uniqueChars == countOfUniqueCharsAtLeastK:
                    res = max(res, fast - slow)
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