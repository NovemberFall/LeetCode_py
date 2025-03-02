class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map.setdefault(key, [])
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ''
        cur_list = self.map[key]
        index = self.binary_search(cur_list, timestamp)
        if index == -1:
            return ''
        return cur_list[index][1]

    def binary_search(self, cur_list, timestamp):
        left, right = 0, len(cur_list) - 1
        while left < right - 1:
            mid = (left + right) >> 1
            if cur_list[mid][0] <= timestamp:
                left = mid
            else:
                right = mid - 1

        if cur_list[right][0] <= timestamp:
            return right
        if cur_list[left][0] <= timestamp:
            return left
        return -1

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)