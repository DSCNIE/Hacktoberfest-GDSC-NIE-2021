# Author: @Iresharma
# https://leetcode.com/problems/shuffle-the-array/submissions/

"""
Runtime: 52 ms, faster than 95.92% of Python3 online submissions for Shuffle the Array.
Memory Usage: 14.5 MB, less than 48.50% of Python3 online submissions for Shuffle the Array.
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        final = []
        for i in range(n):
            final.append(x[i])
            final.append(y[i])
        return final