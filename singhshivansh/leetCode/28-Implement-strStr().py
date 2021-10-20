# Author: @Iresharma
# https://leetcode.com/problems/28-Implement-strStr()/

"""
Runtime: 20 ms, faster than 99.25% of Python3 online submissions for Implement strStr().
Memory Usage: 14.6 MB, less than 23.78% of Python3 online submissions for Implement strStr().
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1