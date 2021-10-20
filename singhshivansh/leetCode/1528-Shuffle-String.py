# Author: @Iresharma
# https://leetcode.com/problems/shuffle-string/

"""
Runtime: 52 ms, faster than 81.37% of Python3 online submissions for Shuffle String.
Memory Usage: 14.2 MB, less than 51.95% of Python3 online submissions for Shuffle String.
"""

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ret = list(s)
        for i in range(len(s)):
            ret[indices[i]] = s[i]
        return ''.join(ret)