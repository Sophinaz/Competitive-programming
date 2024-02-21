# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return
        curr = head
        def remove(curr,val):
            temp = curr
            if not curr.next:
                if curr.val == val: return 
                else: return curr
            
            if curr.val == val:
                return remove(curr.next,val)
            else:
                temp.next = remove(curr.next,val)
                return temp
        return remove(curr,val)
        