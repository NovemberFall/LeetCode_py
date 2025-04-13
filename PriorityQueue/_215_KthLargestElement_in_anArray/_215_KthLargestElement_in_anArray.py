import heapq  # Import the heapq module for priority queue (min-heap) operations
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []  # Create an empty list to represent the min-heap

        for num in nums:
            heapq.heappush(minHeap, num)  # Add the element to the min-heap

            if len(minHeap) > k:
                heapq.heappop(minHeap)   # Remove the smallest element if the size exceeds k

        return minHeap[0]  # The top of the min-heap is the kth largest element
