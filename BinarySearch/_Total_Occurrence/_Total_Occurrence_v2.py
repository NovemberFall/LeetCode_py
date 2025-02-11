class Solution(object):
    def totalOccurrence(self, array, target):
        """
        input: int[] array, int target
        return: int
        """
        # write your solution here
        if not array or len(array) == 0:
            return 0
        first = self.firstOccurrence(array, target)
        last = self.lastOccurrence(array, target)
        return 0 if first == -1 else last - first + 1

    def firstOccurrence(self, array, target):
        left, right = 0, len(array) - 1
        idx = -1
        while left <= right:
            mid = (left + right) >> 1
            if array[mid] == target:
                idx = mid
                right = mid - 1
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return idx

    def lastOccurrence(self, array, target):
        left, right = 0, len(array) - 1
        idx = -1
        while left <= right:
            mid = (left + right) >> 1
            if array[mid] == target:
                idx = mid
                left = mid + 1
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return idx



