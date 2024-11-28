class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        if not s or n == 0:
            return ""

        # Forward pass to remove invalid closing parentheses ')'
        sb = []
        cnt = 0
        for i in range(n):
            c = s[i]
            if c == '(':
                sb.append(c)
                cnt += 1
            elif c == ')' and cnt > 0:
                sb.append(c)
                cnt -= 1
            elif c == ')' and cnt == 0:
                continue
            elif c != ')':  # "x x ( x x"
                sb.append(c)

        print("".join(sb))  # Output intermediate result: le(e(t(co)de)

        # Backward pass to remove invalid opening parentheses '('
        filtered = []
        for i in range(len(sb) - 1, -1, -1):
            c = sb[i]
            if c == '(' and cnt > 0:
                cnt -= 1
            else:
                filtered.append(sb[i])

        return "".join(filtered[::-1])


if __name__ == "__main__":
    soln = Solution()
    s = "le(e(t(co)de)"
    print(soln.minRemoveToMakeValid(s))
