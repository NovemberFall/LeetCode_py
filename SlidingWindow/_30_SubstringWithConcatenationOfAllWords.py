from collections import defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        n = len(s)
        wordLen = len(words[0])
        wordNum = len(words)
        totalLen = wordNum * wordLen

        if not words or n < wordNum * wordLen:
            return res

        allSeen = self.buildMap(words)

        for i in range(wordLen):
            left = i
            right = i
            count = 0
            curSeen = defaultdict(int)

            while right + wordLen <= n:
                cur = s[right:right + wordLen]
                right += wordLen

                if cur in allSeen:
                    curSeen[cur] += 1
                    count += 1

                    while curSeen[cur] > allSeen[cur]:
                        delete = s[left: left + wordLen]
                        curSeen[delete] -= 1
                        left += wordLen
                        count -= 1
                else:
                    left = right
                    curSeen.clear()
                    count = 0

                if count == wordNum:
                    res.append(left)
        return res

    # Store the frequency of each word in words
    def buildMap(self, words):
        wordMap = defaultdict(int)
        for word in words:
            wordMap[word] += 1
        return wordMap
