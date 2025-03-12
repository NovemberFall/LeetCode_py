class Solution(object):
    def mergeSort(self, array):
        """
        input: int[] array
        return: int[]
        """
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = self.mergeSort(array[:mid])
        right = self.mergeSort(array[mid:])
        return self.merge(left, right)

    def merge(self, leftHalf, rightHalf):
        i, j = 0, 0
        res = []
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                res.append(leftHalf[i])
                i += 1
            else:
                res.append(rightHalf[j])
                j += 1

        while i < len(leftHalf):
            res.append(leftHalf[i])
            i += 1
        while j < len(rightHalf):
            res.append(rightHalf[j])
            j += 1
        return res