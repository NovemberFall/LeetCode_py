class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue

            if abbr[j] <= '0' or abbr[j] > '9':
                return False

            start = j
            while j < len(abbr) and abbr[j] >= '0' and abbr[j] <= '9':
                j += 1

            num = int(abbr[start:j])
            i += num

        return i == len(word) and j == len(abbr)