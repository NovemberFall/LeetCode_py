from typing import List


class Solution:
    def restoreIpAddresses(self, s) -> List[str]:
        res = []
        if 3 > len(s) or len(s) > 12:
            return res

        sb = list(s)
        self.dfs(res, sb, 0, 0)
        return res

    def dfs(self, res, sb, start_idx, dot_nums) -> None:
        if dot_nums == 3:
            if self.is_valid(sb[start_idx:]):
                res.append("".join(sb))
            return

        for i in range(start_idx, len(sb)):
            if self.is_valid(sb[start_idx:i + 1]):
                sb.insert(i + 1, ".")
                dot_nums += 1
                self.dfs(res, sb, i + 2, dot_nums)
                dot_nums -= 1
                del sb[i + 1]

    def is_valid(self, s) -> bool:
        if not s or len(s) > 3:
            return False
        if s[0] == '0' and len(s) > 1:
            return False
        if int("".join(s)) > 255:
            return False
        return True
