class Solution:

  def checkValidString(self, s: str) -> bool:
    # min_op: minimum possible number of unmatched '('
    # max_op: maximum possible number of unmatched '('
    min_op = 0
    max_op = 0

    for char in s:
      if char == "(":
        min_op += 1
        max_op += 1
      elif char == ")":
        min_op -= 1
        max_op -= 1
      else:  # char == '*'
        # '*' acts as ')' -> min_op decreases
        # '*' acts as '(' -> max_op increases
        # '*' acts as ''  -> bounds stay within this widened range
        min_op -= 1
        max_op += 1

      # If max_op drops below 0, even treating every '*' as '('
      # cannot balance the excess ')' seen so far.
      if max_op < 0:
        return False

      # min_op cannot be negative because we can't have negative unmatched '(';
      # it means excess '*' were treated as empty instead of ')'.
      if min_op < 0:
        min_op = 0

    # Valid if it is possible to balance all '(' (i.e., minimum unmatched reaches 0)
    return min_op == 0
