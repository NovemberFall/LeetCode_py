class Solution(object):
    def quickSort(self, array):
        """
        input: int[] array
        return: int[]
        """
        self.quick_sort(array, 0, len(array) - 1)
        return array

    def quick_sort(self, array, left, right):
        if left >= right:
            return
        pivot = self.partition(array, left, right)
        self.quick_sort(array, left, pivot - 1)
        self.quick_sort(array, pivot + 1, right)

    def partition(self, array, left, right):
        leftBound = left
        rightBound = right - 1
        import random
        rand = random.randint(leftBound, rightBound)
        array[rand], array[right] = array[right], array[rand]
        pivot = array[right]
        while leftBound <= rightBound:
            if array[leftBound] < pivot:
                leftBound += 1
            elif array[rightBound] >= pivot:
                rightBound -= 1
            elif array[leftBound] >= pivot and array[rightBound] < pivot:
                array[leftBound], array[rightBound] = array[rightBound], array[leftBound]
                leftBound += 1
                rightBound -= 1
        array[leftBound], array[right] = array[right], array[leftBound]
        return leftBound
