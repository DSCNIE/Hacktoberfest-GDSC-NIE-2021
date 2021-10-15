# Author: @Iresharma
# https://leetcode.com/problems/34-Find-First-and-Last-Position-of-Element-in-Sorted-Array/

"""
Runtime: 80 ms, faster than 89.10% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.4 MB, less than 79.72% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        return [nums.index(target), len(nums) - 1 - nums[::-1].index(target)]