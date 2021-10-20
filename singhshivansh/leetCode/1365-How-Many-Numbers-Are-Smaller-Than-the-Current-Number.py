# Author: @Iresharma
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

"""
Runtime: 48 ms, faster than 96.47% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
Memory Usage: 14.3 MB, less than 43.76% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dp = {}
        seq = sorted(nums)
        print(seq)
        ret = []
        for i in nums:
            try:
                ret.append(dp[i])
            except:
                index = seq.index(i)
                ret.append(index)
                dp[i] = index
        return ret