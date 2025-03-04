from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        curr_line = []
        curr_len = 0

        for word in words:
            # Check if adding this word would exceed the maxWidth
            if curr_len + len(word) + len(curr_line) > maxWidth:
                # If yes, we need to justify the current line
                if len(curr_line) == 1:
                    # Special case: only one word in the line
                    res.append(curr_line[0] + ' ' * (maxWidth - len(curr_line[0])))
                else:
                    # Distribute spaces evenly
                    total_spaces = maxWidth - curr_len
                    space_between_words = total_spaces // (len(curr_line) - 1)
                    extra_spaces = total_spaces % (len(curr_line) - 1)

                    line = curr_line[0]
                    for i in range(1, len(curr_line)):
                        if i <= extra_spaces:
                            spaces = ' ' * (space_between_words + 1)
                        else:
                            spaces = ' ' * (space_between_words)
                        line += spaces + curr_line[i]

                    res.append(line)

                # Reset for the next line
                curr_line = [word]
                curr_len = len(word)
            else:
                # Add word to the current line
                curr_line.append(word)
                curr_len += len(word)

        # Handle the last line (left-justified)
        last_line = ' '.join(curr_line)
        res.append(last_line + ' ' * (maxWidth - len(last_line)))

        return res