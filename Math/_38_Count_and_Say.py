import itertools


class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(n-1):
            addtional = ''
            for digit, group in itertools.groupby(res):
                count = len(list(group))
                # addtional += "%i%s" % (count, digit)
                addtional += f"{count}{digit}"
            res = addtional
        return res
