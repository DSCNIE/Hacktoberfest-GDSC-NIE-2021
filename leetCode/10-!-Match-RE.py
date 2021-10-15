# Author: @Iresharma
# https://leetcode.com/problems/regular-expression-matching/submissions/


# ! NEED BETTER SOLUTION

'''
Runtime: 60 ms, faster than 43.99% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 14.3 MB, less than 56.91% of Python3 online submissions for Regular Expression Matching.
'''

import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        z = re.findall(p, s)
        if z and z[0] == s:
            return True
        return False