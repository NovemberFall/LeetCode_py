import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        maxHeap = []  # Use a list to simulate a max-heap

        for point in points:
            distance_sq = point[0]**2 + point[1]**2
            # Python's heapq is a min-heap, so we store the negative distance
            # to simulate a max-heap based on distance.
            heapq.heappush(maxHeap, (-distance_sq, point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        for _ in range(k):
            neg_distance_sq, point = heapq.heappop(maxHeap)
            res.append(point)

        return res
