# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.answer = True
        dummy = root
        def symmetric(root,dummy):
            if (not root and dummy) or (not dummy and root):
                self.answer = False
                return self.answer
            if not root: return self.answer
            if dummy.val != root.val: 
                self.answer = False
                return self.answer
            symmetric(root.left,dummy.right)
            symmetric(root.right,dummy.left)
            return self.answer
        return symmetric(root,dummy)
