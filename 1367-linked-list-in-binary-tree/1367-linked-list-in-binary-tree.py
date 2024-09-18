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
        if not root: return 
        def checker(node, linked):
            if linked is None: return True
            if node is None or node.val != linked.val: return

            
            return checker(node.left, linked.next) or checker(node.right, linked.next)




        return checker(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
                