class Solution(object):
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        array = list(s)
        end = 0
        # remove space
        for i in range(len(array)):
            if array[i] == ' ' and (i == 0 or array[i - 1] == ' '):
                continue
            array[end] = array[i]
            end += 1
        # Post-processing: it is possible we still have one trailing
        # space character at the end.
        if end > 0 and array[end - 1] == ' ':
            end -= 1

        # Reverse words
        # 1. reverse the whole char aray
        self.reverse(array, 0, end - 1)
        start = 0
        # 2. reverse each of the words
        for i in range(end):
            # the start index of a word.
            if array[i] != ' ' and (i == 0 or array[i - 1] == ' '):
                start = i
            # the end index of a word
            if array[i] != ' ' and (i == end - 1 or array[i + 1] == ' '):
                self.reverse(array, start, i)
        return "".join(array[:end])

    def reverse(self, array, left, right):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1