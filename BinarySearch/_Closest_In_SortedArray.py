class Solution(object):
  def closest(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    if array is None or len(array) == 0:
        return -1
    left, right = 0, len(array) - 1
    while left < right - 1:
        mid = (left + right) >> 1
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid
        else:
            right = mid

    if abs(array[left] - target) <= abs(array[right] - target):
        return left
    else:
        return right