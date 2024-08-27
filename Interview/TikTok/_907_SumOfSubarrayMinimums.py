from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        prev_smaller = [-1] * n
        next_smaller = [n] * n

        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)

        mod = 10**9 + 7
        ans = 0

        for i in range(n):
            ans += (i - prev_smaller[i]) * (next_smaller[i] - i) * arr[i]
            ans %= mod

        return int(ans)



