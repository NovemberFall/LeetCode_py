class Solution(object):
  def exist(self, a, b, c, target):
    """
    input: int[] a, int[] b, int[] c, int target
    return: boolean
    """
    # write your solution here
    s = set(a)
    for num_b in b:
      for num_c in c:
        if target - num_b - num_c in s:
          return True
    return False