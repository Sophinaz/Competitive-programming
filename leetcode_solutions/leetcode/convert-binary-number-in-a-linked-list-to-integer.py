# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count = 0
        first = head
        while first:
            count += 1
            first = first.next
        result = 0
        count -= 1
        while head:
            result += head.val * (2**count)
            count-=1
            head = head.next

        return result