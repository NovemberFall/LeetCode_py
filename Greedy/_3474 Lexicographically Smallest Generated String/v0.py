class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        ans = ['?'] * (n + m - 1)  # ? 表示待定位置

        # 处理 T
        for i, b in enumerate(str1):
            if b != 'T':
                continue
            # 子串必须等于 str2
            for j, c in enumerate(str2):
                v = ans[i + j]
                if v != '?' and v != c:
                    return ""
                ans[i + j] = c

        old_ans = ans
        ans = ['a' if c == '?' else c for c in ans]  # 待定位置的初始值为 a

        # 处理 F
        for i, b in enumerate(str1):
            if b != 'F':
                continue
            # 子串必须不等于 str2
            if ''.join(ans[i: i + m]) != str2:
                continue
            # 找最后一个待定位置
            for j in range(i + m - 1, i - 1, -1):
                if old_ans[j] == '?':  # 之前填 a，现在改成 b
                    ans[j] = 'b'
                    break
            else:
                return ""

        return ''.join(ans)