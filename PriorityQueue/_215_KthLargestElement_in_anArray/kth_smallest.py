import heapq
from typing import List


class Solution:
    def kSmallest(self, nums: List[int], k: int) -> int:
        if not nums or k <= 0 or k > len(nums):
            return -1

        # Max heap to store kth smallest elements (we invert to use Python's min-heap)
        res = [-elem for elem in nums[0:k]]
        heapq.heapify(res)
        for i in range(k, len(nums)):
            if -res[0] > nums[i]:  # if current element is smaller than largest in heap
                heapq.heappop(res)
                heapq.heappush(res, -nums[i])
        # Top of the max heap is the kth smallest (in negative)
        return -res[0]
