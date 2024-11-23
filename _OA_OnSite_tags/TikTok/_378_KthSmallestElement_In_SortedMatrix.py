import heapq
from typing import List

class Cell:
    def __init__(self, row: int, col: int, val: int):
        self.row = row
        self.col = col
        self.val = val

    # Define the comparator for the min heap based on the cell value
    def __lt__(self, other):
        if self.val < other.val:
            return True
        # return self.val < other.val

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # minHeap initialization
        minHeap = []
        heapq.heappush(minHeap, Cell(0, 0, matrix[0][0]))

        # Visited array to avoid processing the same cell twice
        visited = [[False] * cols for _ in range(rows)]
        visited[0][0] = True

        # Process the first k-1 smallest elements
        for _ in range(k - 1):
            cur = heapq.heappop(minHeap)

            # Check the downward neighbor
            if cur.row + 1 < rows and not visited[cur.row + 1][cur.col]:
                heapq.heappush(minHeap, Cell(cur.row + 1, cur.col, matrix[cur.row + 1][cur.col]))
                visited[cur.row + 1][cur.col] = True

            # Check the rightward neighbor
            if cur.col + 1 < cols and not visited[cur.row][cur.col + 1]:
                heapq.heappush(minHeap, Cell(cur.row, cur.col + 1, matrix[cur.row][cur.col + 1]))
                visited[cur.row][cur.col + 1] = True

        return minHeap[0].val