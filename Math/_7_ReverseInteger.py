class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x

        res = 0
        while x > 0:
            digit = x % 10
            x //= 10
            if res > (2 ** 31 - 1 - digit) // 10:
                return 0
            res = (res * 10) + digit

        return -res if is_negative else res
