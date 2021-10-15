# Author: @Iresharma
# https://leetcode.com/problems/1614-Maximum-Nesting-Depth-of-the-Parentheses/

"""
Runtime: 32 ms, faster than 61.70% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
Memory Usage: 14.3 MB, less than 39.61% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        if s.count('(') == 0:
            return 0
        stack = []
        maxcount, count = 0, 0
        filtered = s[s.index('('): len(s) - (s[::-1].index(')'))]
        print(filtered)
        for i in filtered:
            if i == '(':
                stack.append(1)
                count += 1
            elif i == ')':
                maxcount = max(maxcount, count)
                stack.pop()
                count -= 1
                if len(stack) == 0:
                    count = 0
        return maxcount