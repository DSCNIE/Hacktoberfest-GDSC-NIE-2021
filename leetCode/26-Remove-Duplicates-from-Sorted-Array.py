# Author: @Iresharma
# https://leetcode.com/problems/26-Remove-Duplicates-from-Sorted-Array/

"""
Runtime: 80 ms, faster than 82.97% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.7 MB, less than 92.17% of Python3 online submissions for Remove Duplicates from Sorted Array
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        lNums = len(nums)
        for i in range(1, lNums):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        return index + 1