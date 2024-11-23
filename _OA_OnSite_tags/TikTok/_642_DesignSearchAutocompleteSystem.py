import heapq
from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None] * 27  # Array to hold 26 letters + 1 space
        self.counts = defaultdict(int)  # Dictionary to store sentences and their frequencies

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.current_input = []

        # Initialize the Trie with given sentences and times
        for sentence, time in zip(sentences, times):
            self.add_sentence(sentence, time)

    def add_sentence(self, sentence, frequency) -> None:
        node = self.root
        for char in sentence:
            index = 26 if char == ' ' else ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
            node.counts[sentence] += frequency

    def input(self, c: str) -> List[str]:
        if c == '#':
            # End of input, add the current input sentence to Trie
            sentence = ''.join(self.current_input)
            self.add_sentence(sentence, 1)
            self.current_input = []  # Reset input buffer
            return []

        self.current_input.append(c)   # Append current character to the ongoing sentence
        node = self.root

        # Traverse the Trie based on the current input characters
        for char in self.current_input:
            index = 26 if char == ' ' else ord(char) - ord('a')
            if not node.children[index]:
                return []  # Return empty list if prefix doesn't match
            node = node.children[index]

        # Use a priority queue to retrieve the top 3 results
        pq = []
        for sentence, frequency in node.counts.items():
            heapq.heappush(pq, (-frequency, sentence))  # Push negative frequency for max-heap
            if len(pq) > 3:
                heapq.heappop(pq)

        # Extract top sentences and sort them lexicographically if needed
        res = []
        while pq:
            res.append(heapq.heappop(pq)[1])

        return res[::-1]  # Reverse to return the sentences in correct order



























