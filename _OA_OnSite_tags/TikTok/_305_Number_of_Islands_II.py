from typing import List


class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
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

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        uf = UnionFind(m * n)
        grid = [[False] * n for _ in range(m)]
        res = []
        count = 0

        for row, col in positions:
            if grid[row][col]:
                res.append(count)
                continue

            grid[row][col] = True
            count += 1
            index = row * n + col

            for d in directions:
                cur_row, cur_col = row + d[0], col + d[1]
                if cur_row < 0 or cur_row >= m or cur_col < 0 or cur_col >= n or grid[cur_row][cur_col] == False:
                    continue

                newIndex = cur_row * n + cur_col
                if not uf.connected(index, newIndex):
                    uf.union(index, newIndex)
                    count -= 1
            res.append(count)

        return res



