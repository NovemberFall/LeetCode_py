class Solution:
    def __init__(self):
        self.index = 0

    def decodeString(self, s: str) -> str:
        res = []
        while self.index < len(s) and s[self.index] != ']':
            if not s[self.index].isdigit():
                res.append(s[self.index])
                self.index += 1
            else:
                k = 0
                while self.index < len(s) and s[self.index].isdigit():
                    k = k * 10 + int(s[self.index])
                    self.index += 1
                self.index += 1
                sub_str = self.decodeString(s)
                self.index += 1
                for _ in range(k):
                    res.append(sub_str)

        return "".join(res)

