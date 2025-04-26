from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Sort the heaters list to efficiently find the nearest ones using binary search.
        heaters.sort()
        res = 0

        # Iterate through each house to find the minimum distance to a heater.
        for house in houses:
            # The binary search returns the index of the largest heater <= house
            i = self.binarySearch(heaters, house)
            # The heater potentially to the right of the house is at index i + 1.
            j = i + 1
            left_distance = float('inf') if i < 0 else house - heaters[i]
            right_distance = float('inf') if j >= len(heaters) else heaters[j] - house

            # The minimum radius required for the current house is the minimum of the distances to the left and right heaters.
            cur_distance = min(left_distance, right_distance)

            # Update the overall maximum radius needed if the current house requires a larger radius.
            res = max(res, cur_distance)
        return res

    def binarySearch(self, heaters: List[int], target: int) -> int:
        left, right = 0, len(heaters) - 1
        if heaters[left] > target:
            return -1
        while left < right - 1:
            mid = (left + right) >> 1
            if heaters[mid] == target:
                return mid
            elif heaters[mid] < target:
                left = mid
            else:
                right = mid - 1

        # After the loop, check the remaining one or two elements (at left and right).
        # Return the index of the largest heater that is less than or equal to the target.
        return right if heaters[right] <= target else left


