import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            meeting = intervals[i]
            if free_rooms[0] <= meeting[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, meeting[1])
        return len(free_rooms)
