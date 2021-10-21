# Author: @Iresharma
# https://leetcode.com/problems/1689-Partitioning-Into-Minimum-Number-Of-Deci-Binary-Numbers/

"""
"""

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(map(int, list(n)))