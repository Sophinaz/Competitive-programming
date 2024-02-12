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
        curr = node
        fast = node

        count = 0
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            curr = curr.next

        curr.next = curr.next.next
        
        if node.next: return node.next
        else: return 