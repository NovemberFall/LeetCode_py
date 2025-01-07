from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        start = [interval[0] for interval in intervals]
        end = [interval[1] for interval in intervals]

        start.sort()
        end.sort()

        res = 0
        room = 0
        start_index = 0
        end_index = 0

        while start_index < len(intervals):
            if start[start_index] < end[end_index]:
                start_index += 1
                room += 1
            else:
                end_index += 1
                room -= 1
            res = max(res, room)
        return res