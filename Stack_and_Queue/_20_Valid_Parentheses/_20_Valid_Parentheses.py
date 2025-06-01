class Solution(object):
    def isValid(self, s: str):
        res = []
        match = {'(': ')', '{': '}', '[': ']'}
        for p in s:
            if p in match:  # If it's an opening bracket
                res.append(p)
            elif not res or match[res[-1]] != p:  # If stack is empty or top does not match
                return False
            elif match[res[-1]] == p:
                res.pop()  # Remove the last opening bracket as it matched correctly
        return not res  # Return True if stack is empty (all matched)
