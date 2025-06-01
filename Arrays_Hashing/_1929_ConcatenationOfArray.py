from typing import List

class concatenation:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(2):
            for n in nums:
                res.append(n)

        return res
