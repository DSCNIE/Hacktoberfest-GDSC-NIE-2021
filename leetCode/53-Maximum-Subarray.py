# Author: @Iresharma
# https://leetcode.com/problems/maximum-subarray/

"""
Runtime: 60 ms, faster than 90.50% of Python3 online submissions for Maximum Subarray.
Memory Usage: 15 MB, less than 36.41% of Python3 online submissions for Maximum Subarray.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        
        tmpsum = nums[0]
        maxx = nums[0]
        
        for i in range(1, len(nums)):
            n = nums[i]
            if tmpsum + n > n:
                tmpsum += n
            else:
                tmpsum = n
            
            if tmpsum > maxx:
                maxx = tmpsum
        
        return maxx