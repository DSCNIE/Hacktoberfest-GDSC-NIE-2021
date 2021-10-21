# Author: @Iresharma
# https://leetcode.com/problems/reverse-integer/

"""
Runtime: 20 ms, faster than 99.38% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.2 MB, less than 71.79% of Python3 online submissions for Reverse Integer.
"""

class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) > 2147483648:
            return 0
        s = str(x)
        if s[0] == '-':
            x = int('-' + s[::-1][:-1:])
            return x if abs(x) < 2147483648 else 0
        x = int(s[::-1])
        return x if x < 2147483648 else 0