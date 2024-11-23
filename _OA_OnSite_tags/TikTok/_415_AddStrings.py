class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i, j = len(num1) - 1, len(num2) - 1
        carry, sum = 0, 0

        while i >= 0 or j >= 0 or carry > 0:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            sum = digit1 + digit2 + carry

            res.append(str(sum % 10))
            carry = sum // 10
            i -= 1
            j -= 1

        return "".join(res[::-1])