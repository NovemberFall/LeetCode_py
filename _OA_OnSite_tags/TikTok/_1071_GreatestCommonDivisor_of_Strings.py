from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated __strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""

        # If __strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        return str1[0:gcd(len(str1), len(str2))]


