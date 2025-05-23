class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if str1 == "":
            return str2
        if str2 == "":
            return str1
        if str1[-1] == str2[-1]:  # current 最短公共超序列一定包含 s[-1]
            return self.shortestCommonSupersequence(str1[:-1], str2[:-1]) + str1[-1]
        else:
            pick_str1 = self.shortestCommonSupersequence(str1[:-1], str2) + str1[-1]
            pick_str2 = self.shortestCommonSupersequence(str1, str2[:-1]) + str2[-1]
            if len(pick_str1) < len(pick_str2):
                return pick_str1
            else:
                return pick_str2

