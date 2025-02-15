class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 0, x
        res = x
        while left <= right:
            mid = (left + right) >> 1
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res