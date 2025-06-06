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
            res = 0
            if not is_num:  # 选择跳过，不填数字
                res = f(i + 1, mask, False, False)

            up = int(s[i]) if is_limit else 9
            for d in range(0 if is_num else 1, up + 1):
                if mask >> d & 1 == 0:  # mask 里有没有 d
                    res += f(i + 1, mask | (1 << d), is_limit and d == up, True)
            return res

        return f(0, 0, True, False)









'''
    OR:
'''


# class Solution:
#     def countSpecialNumbers(self, n: int) -> int:
#         # Digit DP
#         s = str(n)
#
#         # is_limit
#         @cache
#         def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
#             if i == len(s):
#                 return int(is_num)  # 之前如果填过一个数字 就返回1
#             res = 0
#             if not is_num:  # 选择跳过，不填数字
#                 res = f(i + 1, mask, False, False)
#
#             up = int(s[i]) if is_limit else 9
#             for d in range(1 - int(is_num), up + 1):
#                 if mask >> d & 1 == 0:  # mask 里有没有 d
#                     res += f(i + 1, mask | (1 << d), is_limit and d == up, True)
#             return res
#
#         return f(0, 0, True, False)