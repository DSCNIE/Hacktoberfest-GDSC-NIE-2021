# Author: @Iresharma
# https://leetcode.com/problems/longest-common-prefix

"""
Runtime: 32 ms, faster than 77.94% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.5 MB, less than 24.77% of Python3 online submissions for Longest Common Prefix.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        checkLen = len(strs[0])
        check = [False for i in range(len(strs))]
        i = 0
        checkstr = strs[0]
        while False in check and checkLen - i >= 0:
            checkstr = strs[0][:checkLen - i]
            print(checkstr)
            check = list(map(lambda x: checkstr == x[:checkLen - i], strs))
            i += 1
        return checkstr