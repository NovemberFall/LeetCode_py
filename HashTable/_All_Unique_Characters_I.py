class Solution(object):
    def allUnique(self, word):
        """
        input: string word
        return: boolean
        """
        # write your solution here
        dict = set()
        for c in word:
            if c in dict:
                return False
            dict.add(c)
        return True
