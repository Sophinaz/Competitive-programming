# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.count = 0
        cur  = head
        while cur != None:
            cur = cur.next
            self.count += 1

        n = self.count //2 
        cur = head
        
        for _ in range(n):
            cur  = cur.next
        return cur