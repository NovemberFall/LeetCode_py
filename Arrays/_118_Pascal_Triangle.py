from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res

# Main method to test with numRows = 5
if __name__ == "__main__":
    solution = Solution()
    result = solution.generate(5)

    # Print the resulting Pascal's Triangle
    for row in result:
        print(row)