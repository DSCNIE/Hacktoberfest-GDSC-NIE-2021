# Author: @Iresharma
# https://leetcode.com/problems/17-Letter-Combinations-of-a-Phone-Number/

"""
Runtime: 28 ms, faster than 83.42% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14 MB, less than 99.51% of Python3 online submissions for Letter Combinations of a Phone Number.
"""

from itertools import permutations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        x = len(digits)
        if x == 0:
            return []
        
        def singleTomul(a, b):
            return "".join(list(map(lambda x: a+x, b)))

            
        letter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if x == 1:
            return list(letter[digits])
        something = list(letter[digits[0]])
        ret = []
        for i in digits[1:]:
            for j in letter[i]:
                ret += list(map(lambda x: singleTomul(x, j), something))
            something = ret
            ret = []
        return something
        