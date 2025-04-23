import heapq


class MedianFinder:

    def __init__(self):
        self.larger = []
        self.smaller = []
        self.even = True

    def addNum(self, num: int) -> None:
        if self.even:
            heapq.heappush(self.larger, -num)  # Use negative for max-heap
            top_of_larger = -heapq.heappop(self.larger)
            heapq.heappush(self.smaller, top_of_larger)
        else:
            heapq.heappush(self.smaller, num)
            top_of_smaller = -heapq.heappop(self.smaller)
            heapq.heappush(self.larger, top_of_smaller)
        self.even = not self.even

    def findMedian(self) -> float:
        if self.even:
            return (self.smaller[0] - self.larger[0]) / 2
        else:
            return self.smaller[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
