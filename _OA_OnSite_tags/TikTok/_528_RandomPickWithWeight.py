from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.wSums = w

    def pickIndex(self) -> int:
        # Generate a random number between 1 and the last element in wSums (inclusive)
        weight = random.randint(1, self.wSums[-1])
        left, right = 0, len(self.wSums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if self.wSums[mid] == weight:
                return mid
            elif self.wSums[mid] < weight:
                left = mid + 1
            else:
                right = mid - 1
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()