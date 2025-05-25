class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        def is_valid(segment: str) -> bool:
            if len(segment) == 0 or len(segment) > 3:
                return False
            if segment[0] == '0' and len(segment) > 1:
                return False
            if int(segment) > 255:
                return False
            return True

        res = []
        n = len(s)
        for i in range(1, 4):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    if k >= n:
                        continue
                    s1, s2, s3, s4 = s[:i], s[i:j], s[j:k], s[k:]
                    if all(map(is_valid, [s1, s2, s3, s4])):
                        res.append(f"{s1}.{s2}.{s3}.{s4}")
        return res
