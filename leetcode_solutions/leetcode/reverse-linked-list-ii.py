# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        first = head
        if not head.next: return head
        
        count = 2
        while count < left:
            first = first.next
            count += 1
        
        later = first
        later1= first.next
        if left == 1:
            first = first
            later1 = first
        else: first = first.next
        second = first.next
        count = left
        
        while second and count < right:
            
            temp = second.next
            second.next = first
            first = second
            second = temp
            count += 1

        later1.next = second
        if left == 1: return first
        later.next = first
        return head