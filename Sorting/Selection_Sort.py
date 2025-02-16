from typing import List


class SS_Solution:
    def selection_sort(self, arr: List[int]) -> None:
        n = len(arr)
        # because the last element is the minimum
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr


# Test function
def test_selection_sort():
    ss = SS_Solution()

    # Test case
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)

    ss.selection_sort(arr)

    print("Sorted array:  ", arr)


# Run the test
test_selection_sort()

