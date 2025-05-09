import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a > 0:
            heapq.heappush(maxHeap, (-a, 'a'))
        if b > 0:
            heapq.heappush(maxHeap, (-b, 'b'))
        if c > 0:
            heapq.heappush(maxHeap, (-c, 'c'))

        res = []
        while maxHeap:
            temp_count, char = heapq.heappop(maxHeap)
            count = -temp_count
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not maxHeap:
                    break
                temp_count2, char2 = heapq.heappop(maxHeap)
                res.append(char2)
                count2 = -temp_count2
                count2 -= 1
                if count2 > 0:
                    heapq.heappush(maxHeap, (-count2, char2))
            else:
                count -= 1
                res.append(char)

            if count > 0:
                heapq.heappush(maxHeap, (-count, char))

        return ''.join(res)

