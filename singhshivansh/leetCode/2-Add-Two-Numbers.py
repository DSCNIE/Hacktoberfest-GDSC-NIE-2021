# Author: @Iresharma
# https://leetcode.com/problems/add-two-numbers/

"""
Runtime: 68 ms, faster than 72.26% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.2 MB, less than 90.07% of Python3 online submissions for Add Two Numbers.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.traverseString(l1)
        b = self.traverseString(l2)
        result = str(a + b)[::-1]
        sumL = ListNode()
        start = sumL
        print(result)
        for ind, i in enumerate(result):
            sumL.val = i
            if ind != len(result) - 1:
                nextSumL = ListNode()
                sumL.next = nextSumL
                sumL = nextSumL
        return start
    def traverseString(self, ll: ListNode) -> int:
        num = ""
        while ll != None:
            num = str(ll.val) + num
            ll = ll.next
        return int(num)