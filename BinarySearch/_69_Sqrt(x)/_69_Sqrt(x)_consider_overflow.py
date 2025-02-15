class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x
        res = left
        while left <= right:
            mid = left + (right - left) // 2
            if mid == x // mid:
                return mid
            elif mid < x // mid:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

