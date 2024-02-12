# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        curr = head
        
        if n == count: 
            head = curr.next
            curr.next = None
            return head
        for i in range(count - n-1):
            curr = curr.next
        
        curr.next = curr.next.next
        return head