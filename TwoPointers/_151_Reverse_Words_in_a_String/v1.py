class Solution(object):
    def reverseWords(self, s: str) -> str:
        split_array = s.split(" ")
        return "".join(split_array[::-1])