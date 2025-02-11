from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList:
            return 0
        dict = set(wordList)
        if endWord not in dict:
            return 0

        forwardQueue = set()
        backwardQueue = set()

        forwardQueue.add(beginWord)
        backwardQueue.add(endWord)

        step = 1
        while forwardQueue and backwardQueue:
            if len(forwardQueue) > len(backwardQueue):
                temp = forwardQueue
                forwardQueue = backwardQueue
                backwardQueue = temp
            step += 1
            forwardMutation = set()  # manipulate words via a temp set at current level
            for word in forwardQueue:  # traverse all words from original forwardQueue
                wordChars = list(word)
                for i in range(len(wordChars)):
                    backup = wordChars[i]
                    for c in range(ord('a'), ord('z') + 1):
                        if backup == c:
                            continue
                        wordChars[i] = chr(c)
                        mutation = ''.join(wordChars)
                        if mutation in backwardQueue:
                            return step
                        if mutation in dict:
                            dict.remove(mutation)
                            forwardMutation.add(mutation)
                    wordChars[i] = backup
            forwardQueue = forwardMutation
        return 0
