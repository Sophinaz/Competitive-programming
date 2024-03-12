# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        track = defaultdict(list)
        track[0] = [dummy]
        
        curr = head
        prefix = 0

        while curr:
            prefix += curr.val
            print(prefix, curr.val)
            if prefix in track:
                for i in track[prefix]:
                    i.next = curr.next
            
            track[prefix].append(curr)
            
            curr = curr.next

        return dummy.next

