from typing import List


def bubble_sort(A: List[int]) -> None:
    n = len(A)
    for i in range(n):
        print("level: ", i)
        for j in range(n - 1 - i):  # [0, n)
            # print("compare: ", j)
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                print("after swap: ", A)


alist = [2, 3, 1, 0, 5, -1]
bubble_sort(alist)
print(alist)
