from functools import cache


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        # Digit DP
        s = str(n)

        # is_limit
        @cache
        def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return int(is_num)  # 之前如果填过一个数字 就返回1
            count = 0

            # Option to skip current position (leading zeros or shorter number)
            if not is_num:
                count = f(i + 1, mask, False, False)

            # Determine upper bound for current digit
            upper_bound = int(s[i]) if is_limit else 9

            for dight in range(0 if is_num else 1, upper_bound + 1):
                # Check if digit is already used in mask
                if mask >> dight & 1 == 0:  # mask 里有没有 digit
                    # Add count from placing this digit
                    count += f(i + 1, mask | (1 << dight), is_limit and dight == upper_bound, True)
            return count

        return f(0, 0, True, False)