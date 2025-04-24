import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        size = len(points)
        min_heap = []
        uf = UnionFind(size)

        for i in range(size):
            x1, y1 = points[i]
            for j in range(i + 1, size):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(min_heap, (cost, i, j))

        res = 0
        edges_used = 0

        # Kruskal's Algorithm
        while min_heap and edges_used < size - 1:
            cost, u, v = heapq.heappop(min_heap)
            if not uf.is_connect(u, v):
                uf.union(u, v)
                res += cost
                edges_used += 1
        return res

class UnionFind(object):
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x) -> int:
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

    def is_connect(self, x, y) -> bool:
        return self.find(x) == self.find(y)

