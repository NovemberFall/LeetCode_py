from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        map = defaultdict(list)
        for bus_id in range(len(routes)):
            for stop in routes[bus_id]:
                map[stop].append(bus_id)

        visited_stops = set([source]) # Start with the source stop as visited
        visited_buses = set()  # Track visited buses to avoid cycles
        queue = deque([source])
        res = 0

        while queue:
            res += 1
            size = len(queue)
            for _ in range(size):
                stop = queue.popleft()
                if stop not in map:
                    continue

                for bus in map[stop]:
                    if bus in visited_buses:
                        continue
                    visited_buses.add(bus)

                    for next_stop in routes[bus]:
                        if next_stop == target:
                            return res
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append(next_stop)

        return -1


