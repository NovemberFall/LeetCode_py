from typing import List

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 10

        def insert(self, num):
            node = self
            str_num = str(num)
            for char in str_num:
                if not node.children[ord(char) - ord('0')]:  # or: node.children[int(char)]
                    node.children[ord(char) - ord('0')] = Solution.TrieNode()
                node = node.children[ord(char) - ord('0')]

        def check(self, num):
            node = self
            str_num = str(num)
            length = 0
            for char in str_num:
                if node.children[ord(char) - ord('0')]:
                    length += 1
                else:
                    break
                node = node.children[ord(char) - ord('0')]
            return length

    def __init__(self):
        self.root = self.TrieNode()

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = self.root
        res = 0
        for num in arr1:
            trie.insert(num)

        for num in arr2:
            res = max(res, trie.check(num))

        return res
