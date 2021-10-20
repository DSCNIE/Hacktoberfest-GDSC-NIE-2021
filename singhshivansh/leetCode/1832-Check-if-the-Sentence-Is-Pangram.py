# Author: @Iresharma
# https://leetcode.com/problems/1832-Check-if-the-Sentence-Is-Pangram/

"""
Runtime: 32 ms, faster than 63.09% of Python3 online submissions for Check if the Sentence Is Pangram.
Memory Usage: 14 MB, less than 90.95% of Python3 online submissions for Check if the Sentence Is Pangram.
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        return sorted(set(sentence)) == alpha