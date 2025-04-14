class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(" ".join(s.strip().split()))
        self.reverse(arr, 0, len(arr) - 1)
        print(arr)
        i = 0
        begin, end = 0, 0
        while i < len(arr):
            if i == len(arr) - 1 or arr[i + 1] == " ":
                end = i
                self.reverse(arr, begin, end)
                begin = i + 2
            i += 1
        return "".join(arr)

    def reverse(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1