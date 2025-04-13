"""
    "a a b b a z w" => "abazw"
       i
         j
"""
class Solution:
    def remove_duplicate(self, s: str) -> str:
        if not s or len(s) <= 1:
            return s
        arr = list(s)
        slow, fast = 1, 1
        while fast < len(arr):
            if arr[fast] != arr[slow - 1]:
                arr[slow] = arr[fast]
                slow += 1
            fast += 1
        return "".join(arr[:slow])

