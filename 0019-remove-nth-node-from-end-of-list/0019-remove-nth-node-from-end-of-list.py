# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node:
    def __init__(self,val = None):
        self.val = val
        self.next  = None
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = Node()
        node.next = head
        curr = head
        count = 0
        
        while curr:
            curr = curr.next
            count += 1
        curr = node
        
        for i in range(count - n):
            curr = curr.next
        
        curr.next = curr.next.next
        
        if node.next: return node.next
        else: return 