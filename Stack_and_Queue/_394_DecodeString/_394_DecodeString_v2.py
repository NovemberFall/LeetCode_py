class Solution:
    def decodeString(self, s: str) -> str:
        res_stk = []
        cnt_stk = []
        string = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                count = 0
                while s[i].isdigit():
                    count = count * 10 + int(s[i])
                    i += 1
            elif s[i].isalpha():
                string += s[i]
                i += 1
            elif s[i] == '[':
                cnt_stk.append(count)
                res_stk.append(string)
                string = ""
                i += 1
            else:
                count = cnt_stk.pop()
                last_res = res_stk.pop()
                string = last_res + string * count
                i += 1
        return string