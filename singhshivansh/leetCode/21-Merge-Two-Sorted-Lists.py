# Author: @Iresharma
# https://leetcode.com/problems/merge-two-sorted-lists/submissions/

"""
Runtime: 36 ms, faster than 73.12% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.3 MB, less than 29.06% of Python3 online submissions for Merge Two Sorted Lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        final = ListNode()
        temp = final
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 != None and l2 != None:
            if l1.val >= l2.val:
                temp.val = l2.val
                l2 = l2.next
                temp.next = ListNode()
                temp = temp.next
            else:
                temp.val = l1.val
                l1 = l1.next
                temp.next = ListNode()
                temp = temp.next
        if l1:
            temp.val = l1.val
            temp.next = l1.next
        if l2:
            temp.val = l2.val
            temp.next = l2.next
        return final