from collections import deque
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        dict = set(wordList)
        if endWord not in dict:
            return res
        queue = deque([beginWord])
        graph = {}  # or:   graph = defaultdict(list)
        distance = {}  # or:   distance = {beginWord: 1}
        level = 0
        distance[beginWord] = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                curWord = queue.popleft()
                neighbors = self.getAllNeighbors(dict, curWord)
                if len(neighbors) != 0:
                    for nei in neighbors:
                        if nei not in distance:
                            distance[nei] = level + 1
                            graph.setdefault(nei, [])
                            graph[nei].append(curWord)
                            queue.append(nei)
                        else:
                            if distance[nei] == level + 1:
                                graph[nei].append(curWord)
            level += 1
            if endWord in distance:
                break

        self.dfs(graph, endWord, beginWord, [], res)
        return res

    def getAllNeighbors(self, dict, curWord):
        res = []
        wordChars = list(curWord)
        for i in range(len(wordChars)):
            backup = wordChars[i]
            for c in range(ord('a'), ord('z') + 1):
                if backup == chr(c):
                    continue
                wordChars[i] = chr(c)
                word = "".join(wordChars)
                if word in dict:
                    res.append(word)
            wordChars[i] = backup
        return res

    def dfs(self, graph, endWord, beginWord, path, res):
        if endWord == beginWord:
            path.append(beginWord)
            deepCopy_path = path[::-1]  # firstly deep clone a current path and reverse it
            res.append(deepCopy_path)
            path.pop()
            return

        path.append(endWord)
        if endWord in graph:
            for nei in graph[endWord]:
                self.dfs(graph, nei, beginWord, path, res)
        path.pop()


