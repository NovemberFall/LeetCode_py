class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        leftCount, rightCount = index, (n - index - 1)
        ans = -1

        while left <= right:
            mid = (left + right) >> 1

            leftSum = self.getSum(leftCount, mid - 1)
            rightSum = self.getSum(rightCount, mid - 1)
            totalSum = leftSum + mid + rightSum

            if totalSum > maxSum:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
        return ans


    def getSum(self, countOfElments, val):
        total_sum = 0
        decreasingLen = val

        if (countOfElments >= decreasingLen):
            remainingSum = countOfElments - decreasingLen
            total_sum = self.calc(val) + remainingSum
        else:
            lastVal = decreasingLen - countOfElments
            total_sum = self.calc(val) - self.calc(lastVal)

        return total_sum

    def calc(self, n):
        return n * (n + 1) >> 1


