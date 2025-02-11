class Solution(object):
    def totalOccurrence(self, array, target):
        """
        input: int[] array, int target
        return: int
        """
        # write your solution here
        if array is None or len(array) == 0:
            return 0
        index = self.binarySearch(array, target, 0, len(array) - 1)
        if index == -1:
            return 0
        left = index - 1
        right = index + 1
        total = 1
        while left >= 0 and array[left] == target:
            total += 1
            left -= 1
        while right < len(array) and array[right] == target:
            total += 1
            right += 1
        return total

    def binarySearch(self, array, target, left, right):
        while left <= right:
            mid = (left + right) >> 1
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
