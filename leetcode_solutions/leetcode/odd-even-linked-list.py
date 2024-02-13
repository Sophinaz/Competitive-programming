# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next  : return head

        first = head.next
        odd = head
        count = 1

        while odd.next:
            temp = odd.next
            odd.next = odd.next.next
            track = odd
            odd = temp
            count += 1
        
        if count %2 != 0: 
            odd.next = first
            track.next = None
        else:
            track.next = first
            odd.next = None
        return head