from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Map each stop to the list of buses (routes) that go through it
        # map = defaultdict(list)
        map = {}
        for bus_id in range(len(routes)):
            for stop in routes[bus_id]:
                map.setdefault(stop, []).append(bus_id)

        visited_stops = set([source])  # Keeps track of stops we have visited
        visited_buses = set()          # Keeps track of buses we've already taken
        queue = deque([source])        # Start BFS from the source stop
        res = 0                        # Number of buses taken

        while queue:
            res += 1  # Each level means one more bus taken
            size = len(queue)
            for _ in range(size):
                stop = queue.popleft()

                # if no buses go through this stop, skip
                if stop not in map:
                    continue

                # Explore all buses that go through this stop
                for bus in map[stop]:
                    if bus in visited_buses:
                        continue
                    visited_buses.add(bus)

                    # Add all the stops this bus goes to
                    for next_stop in routes[bus]:
                        if next_stop == target:
                            return res  # Found target, return number of buses taken
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append(next_stop)

        return -1
