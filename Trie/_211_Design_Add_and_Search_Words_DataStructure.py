class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            index = ord(c) - ord('a')
            if cur.children[index] is None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.isWord = True

    def search(self, word: str) -> bool:
        return self.find(word, self.root, 0)

    def find(self, word: str, cur: TrieNode, index: int) -> bool:
        if index == len(word):
            return cur.isWord

        c = word[index]
        if c == '.':  # If wildcard, check all children
            for child in cur.children:
                if child and self.find(word, child, index + 1):
                    return True
            return False
        else:
            child_index = ord(c) - ord('a')
            return cur.children[child_index] is not None and self.find(word, cur.children[child_index], index + 1)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)