# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        prev = ListNode()
        ansA = prev
        nextt = ListNode() 
        ansB = nextt
        while curr:
            temp = curr.next
            if curr.val < x:
                prev.next = curr
                prev = prev.next
            if curr.val >= x:
                nextt.next = curr
                nextt = nextt.next
            curr = temp
        nextt.next = None
        prev.next = ansB.next
        return ansA.next