# Author: @Iresharma
# https://leetcode.com/problems/palindrome-number/submissions/

'''
Runtime: 40 ms, faster than 99.25% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.1 MB, less than 75.69% of Python3 online submissions for Palindrome Number.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string = str(x)
        if string == string[::-1]:
            return True
        return False