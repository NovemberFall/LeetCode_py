import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])

        available = [i for i in range(n)]   # 0, 1, 2, 3, ...
        used = []  # (end_time, room_number)
        count = [0] * n  # count[n] = meetings schedule

        for start, end in meetings:
            # Finish meetings
            while used and used[0][0] <= start:
                __, room_num = heapq.heappop(used)  # since this room is no longer being used
                heapq.heappush(available, room_num)  # add room back to available

            # no room is available
            if not available:
                end_time, room_num = heapq.heappop(used)
                end = end_time + (end - start)  # (end - start) represents duration
                #  end represents new-end time
                heapq.heappush(available, room_num)

            # a room is available
            if available:
                room = heapq.heappop(available)
                heapq.heappush(used, (end, room))
                count[room] += 1

        return count.index(max(count))

