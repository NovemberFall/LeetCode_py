import heapq  # Import the heapq module for priority queue (min-heap) operations
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for i in range(len(nums)):
            if len(res) < k:
                heapq.heappush(res, nums[i])
            else:
                if nums[i] > res[0]:
                    heapq.heappop(res)
                    heapq.heappush(res, nums[i])
        return res[0]
