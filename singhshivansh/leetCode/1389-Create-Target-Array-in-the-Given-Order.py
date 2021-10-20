# Author: @Iresharma
# https://leetcode.com/problems/create-target-array-in-the-given-order

"""
Runtime: 40 ms, faster than 14.62% of Python3 online submissions for Create Target Array in the Given Order.
Memory Usage: 14.1 MB, less than 74.57% of Python3 online submissions for Create Target Array in the Given Order.
"""

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target