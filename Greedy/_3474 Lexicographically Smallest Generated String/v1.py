class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        # The algorithm works in two passes using a greedy approach.
        # 1. It first satisfies all mandatory 'T' constraints.
        # 2. It makes a greedy guess by filling unknowns with 'a'.
        # 3. It then corrects this guess if it violates any 'F' constraints.

        num_constraints = len(str1)
        pattern_len = len(str2)
        word_len = num_constraints + pattern_len - 1

        # Use '?' as a placeholder for unknown characters in the word we are building.
        word_array = ['?'] * word_len

        # --- PASS 1: Apply all 'T' (must-match) constraints ---
        # This pass fills in all characters that are definitively known from the 'T' rules.
        for i, constraint_char in enumerate(str1):
            if constraint_char != 'T':
                continue

            # Place the characters of str2 into the corresponding slice of the word_array.
            for j, char_from_pattern in enumerate(str2):
                char_idx_in_word = i + j
                existing_char = word_array[char_idx_in_word]

                # Check for contradictions: if a different 'T' rule already
                # placed a different character here, a solution is impossible.
                if existing_char != '?' and existing_char != char_from_pattern:
                    return ""

                word_array[char_idx_in_word] = char_from_pattern

        # Save a copy of the array after 'T' rules are applied. This template
        # tells us which characters were originally unknown ('?') vs. fixed by a 'T'.
        template_after_T = list(word_array)

        # Create the initial candidate by greedily filling all remaining unknown slots
        # with 'a' to build the lexicographically smallest possible string.
        candidate_word_array = ['a' if char == '?' else char for char in word_array]

        # --- PASS 2: Correct for 'F' (must-not-match) constraints ---
        # Check if our greedy 'a'-filled guess accidentally violated any 'F' rules.
        for i, constraint_char in enumerate(str1):
            if constraint_char != 'F':
                continue

            current_slice = "".join(candidate_word_array[i: i + pattern_len])

            # If the greedy slice is already NOT equal to str2, the 'F' constraint
            # is satisfied, so we can continue to the next constraint.
            if current_slice != str2:
                continue

            # A VIOLATION OCCURRED: The slice should NOT be str2, but it is.
            # We must change it while keeping the overall string as small as possible.
            # To do this, we make the smallest character change ('a' -> 'b') at the
            # rightmost possible position within the slice.

            # Iterate backwards through the violating slice.
            for j_in_slice in range(pattern_len - 1, -1, -1):
                char_idx_in_word = i + j_in_slice

                # We can only change characters that were originally undetermined ('?').
                # We check our template_after_T to see if this position was fixed.
                if template_after_T[char_idx_in_word] == '?':
                    # We found a modifiable position. Change 'a' to 'b' to fix the violation.
                    candidate_word_array[char_idx_in_word] = 'b'
                    # Once fixed, we can stop trying to change this slice and move on.
                    break
            else:
                # This 'else' belongs to the 'for' loop. It runs only if the loop
                # completed without a 'break'. This means the entire slice was
                # fixed by 'T' rules and we couldn't change any character.
                # This is an unresolvable contradiction.
                return ""

        return "".join(candidate_word_array)