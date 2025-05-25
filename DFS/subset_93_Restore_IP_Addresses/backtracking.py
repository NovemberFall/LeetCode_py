from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)
        def backtrack(start: int, path: List[str]) -> None:
            # If we already have 4 segments but not reached the end of string, it's invalid
            if len(path) > 4:
                return

            # If we have 4 valid segments and used all characters
            if len(path) == 4 and start == n:
                res.append(".".join(path))
                return

            for end in range(start, min(start + 3, n)):
                segment = s[start:end + 1]
                if self.is_valid(segment):
                    path.append(segment)
                    backtrack(end + 1, path)
                    path.pop()  # backtrack

        backtrack(0, [])
        return res


    def is_valid(self, segment) -> bool:
        if len(segment) == 0 or len(segment) > 3:
            return False
        if segment[0] == '0' and len(segment) > 1:
            return False
        if int(segment) > 255:
            return False
        return True