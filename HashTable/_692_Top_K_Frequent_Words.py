from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        return sorted(count.keys(), key=lambda w: (-count[w], w))[:k]
