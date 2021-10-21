# Author: @Iresharma
# https://leetcode.com/problems/valid-parentheses/submissions/

"""
Runtime: 28 ms, faster than 82.37% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.8 MB, less than 99.99% of Python3 online submissions for Valid 
"""

class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        if len(s)%2 != 0:
            return False
        for i in s:
            if i in '[({':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last != pair[i]:
                    return False
        return len(stack) == 0