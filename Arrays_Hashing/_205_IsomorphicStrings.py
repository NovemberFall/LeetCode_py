class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        # s = "AB", t = "CD"
        # zip(s, t) = (A, C), (B, D)
        for c1, c2 in zip(s, t):
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True

if __name__ == "__main__":
    solution = Solution()
    res = solution.isIsomorphic("egg", "add")
    print(res)