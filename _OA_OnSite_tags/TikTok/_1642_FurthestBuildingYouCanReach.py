import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxHeap = []  # max heap of bricks

        for i in range(1, len(heights)):
            climb = heights[i] - heights[i - 1]
            if climb <= 0:
                continue

            heapq.heappush(maxHeap, -climb)
            bricks -= climb

            if bricks < 0 and ladders == 0:
                return i - 1

            if bricks < 0:
                ladders -= 1
                bricks += -heapq.heappop(maxHeap)
        return len(heights) - 1
