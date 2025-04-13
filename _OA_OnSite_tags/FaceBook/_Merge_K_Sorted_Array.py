import heapq


class Solution(object):
    def merge(self, arrayOfArrays):
        """
        input: int[][] arrayOfArrays
        return: int[]
        """
        # write your solution here
        if not arrayOfArrays:
            return arrayOfArrays
        heap = []
        for i in range(len(arrayOfArrays)):
            # insert every first element in each array
            if len(arrayOfArrays[i]):
                heap.append((arrayOfArrays[i][0], i, 0))
        heapq.heapify(heap)
        res = []
        while heap:
            val, index_array, index_element = heapq.heappop(heap)
            res.append(val)
            if index_element < len(arrayOfArrays[index_array]) - 1:
                heapq.heappush(heap,
                               (arrayOfArrays[index_array][index_element + 1], index_array, index_element + 1))
        return res
