# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        track = defaultdict(int)
        while headA:
            if track[headA] != 0:
                return headA
            track[headA] += 1
            headA = headA.next
        while headB:
            if track[headB] != 0:
                return headB
            track[headB] += 1
            headB = headB.next
        return None
