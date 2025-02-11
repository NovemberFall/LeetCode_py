import heapq
from typing import List


'''
     [0, 30], [5, 10], [15, 20]
     
     
'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        minHeap = []  # Stores end times of meetings
        for start, end in intervals:
            # If the earliest meeting in the heap has ended, remove it
            if minHeap and minHeap[0] <= start:
                heapq.heappop(minHeap)
            # Add the current meeting's end time to the heap
            heapq.heappush(minHeap, end)
        return len(minHeap)  # The size of the heap represents the number of rooms needed
