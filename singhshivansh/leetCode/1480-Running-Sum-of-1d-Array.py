# Author: @Iresharma
# https://leetcode.com/problems/running-sum-of-1d-array/submissions/

"""
Runtime: 36 ms, faster than 85.45% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14.3 MB, less than 68.39% of Python3 online submissions for Running Sum of 1d Array.
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_val = 0
        sums = []
        for i in nums:
            sum_val += i
            sums.append(sum_val)
        return sums