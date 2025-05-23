class Solution(object):
    def match(self, input, pattern):
        """
        input: string input, string pattern
        return: boolean
        """
        # write your solution here
        clean_p = self.remove_duplicate_stars(pattern)
        return self.dfs(input, clean_p, {}, 0, 0)

    def remove_duplicate_stars(self, pattern):
        res = []
        for c in pattern:
            if len(res) == 0:
                res.append(c)
                continue
            last_char = res[-1]
            if c == '*' and last_char != '*':
                res.append(c)
            elif c != '*':
                res.append(c)
        return "".join(res)

    def dfs(self, s, p, dp, si, pi):
        key = str(si) + "," + str(pi)
        if key in dp:
            return dp[key]

        if pi == len(p):
            dp[key] = si == len(s)
        elif si == len(s):
            dp[key] = pi + 1 == len(p) and p[pi] == '*'
        elif s[si] == p[pi] or p[pi] == '?':
            dp[key] = self.dfs(s, p, dp, si + 1, pi + 1)
        elif p[pi] == '*':
            match_zero = self.dfs(s, p, dp, si, pi + 1)
            match_one_more = self.dfs(s, p, dp, si + 1, pi)
            dp[key] = match_zero or match_one_more
        elif s[si] != p[pi]:
            dp[key] = False
        return dp[key]



    # Testing Method
    def test_remove_remove_duplicate_stars(self, pattern):
        clean_p = self.remove_duplicate_stars(pattern)
        print(clean_p)

sol = Solution()
sol.test_remove_remove_duplicate_stars("**a**b***c*")  # "*a*b*c*"