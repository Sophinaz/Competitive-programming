# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def checker(node, linked):
            if linked is None: return True
            if node is None: return

            if node.val == linked.val:
                return checker(node.left, linked.next) or checker(node.right, linked.next)
            else:
                return checker(node.left, head) or checker(node.right, head)



        if head == root:
            return checker(root, head.next)
        return checker(root, head)
                