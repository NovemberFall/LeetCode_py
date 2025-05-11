class SnapshotArray:

    def __init__(self, length: int):
        self.snap_cnt = 0
        self.data = [[] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.data[index].append((self.snap_cnt, val))

    def snap(self) -> int:
        self.snap_cnt += 1
        return self.snap_cnt - 1

    def get(self, index: int, snap_id: int) -> int:
        pos = self.binarySearch(self.data[index], snap_id)
        return 0 if pos == -1 else self.data[index][pos][1]

    def binarySearch(self, lst: list, snap_id: int) -> int:
        left, right = 0, len(lst) - 1
        res = -1
        while left <= right:
            mid = (left + right) >> 1
            if lst[mid][0] <= snap_id:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

