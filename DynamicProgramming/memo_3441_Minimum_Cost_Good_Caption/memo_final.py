from functools import cache

class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:  # If caption is shorter than 3, no "good caption" can be formed.
            return ""

        @cache
        def dfs(i: int):
            """
            Returns:
                A tuple (min_cost, best_char, block_len):
                    - min_cost (int): Minimum cost to convert caption[start:] to a good caption
                    - best_char (str): The optimal character to fill the next block
                    - block_len (int): Length of the block using best_char
            """
            if i == n:
                return 0, "", 0

            min_cost = float('inf')
            best_char = ""
            best_len = 0
            best_preview = ""

            # Try all groupings from i to i+2, i+3, i+4 (i.e., group lengths 3 to 5)
            for k in range(i + 2, min(n, i + 5)):
                cost_map = {}

                # Compute the transformation cost for turning all chars in [i:k+1] into each possible char
                for ch in caption[i: k + 1]:
                    total_cost = 0
                    for c_in_block in caption[i: k + 1]:
                        diff = abs(ord(ch) - ord(c_in_block))
                        total_cost += diff
                    cost_map[ch] = total_cost

                # Select the character with the minimum transformation cost
                group_cost = min(cost_map.values())

                # Step 1: Get all characters with the minimal cost
                candidates = []
                for candidate_ch, cost in cost_map.items():
                    if cost == group_cost:
                        candidates.append(candidate_ch)
                # Step 2: Choose the lexicographically smallest character
                group_char = min(candidates)

                group_len = k - i + 1

                # Recursively get the cost and result from the remaining part of the caption
                next_cost, next_char, next_len = dfs(k + 1)

                # Combine the current group and the next group's preview for tie-breaking
                current_preview = (group_char * group_len + next_char * next_len)[:6]

                # Choose the option with lower total cost, or lexicographically smaller preview if tied
                if group_cost + next_cost < min_cost or (group_cost + next_cost == min_cost and current_preview < best_preview):
                    min_cost = group_cost + next_cost
                    best_char = group_char
                    best_len = group_len
                    best_preview = current_preview

            return min_cost, best_char, best_len


        res = []
        idx = 0
        while idx < n:
            _, ch, length = dfs(idx)
            res.append(ch * length)
            idx += length
        return "".join(res)




























