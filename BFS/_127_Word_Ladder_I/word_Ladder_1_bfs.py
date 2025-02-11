from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList:
            return 0

        queue = deque([beginWord])
        dict = set(wordList)
        level = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur == endWord:
                    return level
                chars = list(cur)
                for j in range(len(chars)):
                    originalChar = chars[j]
                    for c in range(ord('a'), ord('z') + 1):
                        chars[j] = chr(c)
                        new_word = ''.join(chars)
                        if new_word in dict:
                            dict.remove(new_word)
                            queue.append(new_word)
                    chars[j] = originalChar
            level += 1
        return 0
