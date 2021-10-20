# Author: @Iresharma
# https://leetcode.com/problems/goal-parser-interpretation/

"""
Runtime: 40 ms, faster than 7.92% of Python3 online submissions for Goal Parser Interpretation.
Memory Usage: 14.3 MB, less than 6.12% of Python3 online submissions for Goal Parser Interpretation.
"""

# * I do not consider this a bad a solution even though its slower compared to others
# I a real dev environment this is the method you'd use to solve such a problem and hence i'd keep this

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)','al')