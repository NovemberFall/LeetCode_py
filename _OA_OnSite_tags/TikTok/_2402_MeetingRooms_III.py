import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # The meetings are sorted by their start time
        print(meetings)

        available = [i for i in range(n)]  # 0 1 2 3
        used = []  # (end_time, room_number)
        count = [0] * n  # count[n] = meetings schedule

        for start, end in meetings:
            # Finish meetings
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            # no room is available
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room)

            # a room is available
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1

        return count.index(max(count))
