# Author: @Iresharma
# https://leetcode.com/problems/multiply-strings/

"""
Runtime: 32 ms, faster than 82.96% of Python3 online submissions for Multiply Strings.
Memory Usage: 14.4 MB, less than 25.89% of Python3 online submissions for Multiply Strings.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = self.convert(num1)
        b = self.convert(num2)
        product = a * b
        return str(product)
    def convert(self, num: str) -> int:
        intDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        count = 1
        finalNum = 0
        for i in num:
            finalNum += intDict[i] * (10**(len(num) - count))
            count += 1
        print(finalNum)
        return finalNum
            