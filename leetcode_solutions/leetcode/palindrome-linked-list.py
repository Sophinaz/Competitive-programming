# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check1 = []

        fast = head
        while fast:
            check1.append(fast.val)
            fast = fast.next
        if check1 == check1[::-1]:
            return True
        else: return False