# Author: @Iresharma
# https://leetcode.com/problems/merge-k-sorted-lists/submissions/

"""
Runtime: 92 ms, faster than 93.57% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 18.4 MB, less than 28.18% of Python3 online submissions for Merge k Sorted Lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if list(map(lambda x: x == None, lists)).count(False) == 0:
            return None
        final = []
        for i in lists:
            while i != None:
                final.append(i.val)
                i = i.next
        final = sorted(final)
        ret = ListNode()
        finalret = ret
        for i in final[:-1:]:
            ret.val = i
            ret.next = ListNode()
            ret = ret.next
        ret.val = final[-1]
        return finalret