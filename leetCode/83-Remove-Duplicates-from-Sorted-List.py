# Author: @Iresharma
# https://leetcode.com/problems/83-Remove-Duplicates-from-Sorted-List/

"""
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


        
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        temp = head
        while temp!= None and temp.next != None:
            if temp.next.val == temp.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head