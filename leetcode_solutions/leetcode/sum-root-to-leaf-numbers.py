# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumnum(node, val=0):
            if not node.left and not node.right: 
                self.answer += ((10*val) + node.val)
                return self.answer

            if node.left: sumnum(node.left,(10*val) + node.val)
            if node.right: sumnum(node.right,(10*val) + node.val)
            return self.answer
        return sumnum(root)
