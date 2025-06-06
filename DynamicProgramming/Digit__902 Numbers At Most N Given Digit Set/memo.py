from functools import cache
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)

        # is_limit
        @cache
        def f(i: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return int(is_num)  # 之前如果填过一个数字 就返回1
            count = 0

            # Option to skip current position (leading zeros or shorter number)
            if not is_num:
                count = f(i + 1, False, False)

            # Determine upper bound for current digit
            upper_bound = s[i] if is_limit else '9'

            for dight in digits:
                if dight > upper_bound:
                    break
                # Add count from placing this digit
                count += f(i + 1, is_limit and dight == upper_bound, True)
            return count

        return f(0, True, False)
