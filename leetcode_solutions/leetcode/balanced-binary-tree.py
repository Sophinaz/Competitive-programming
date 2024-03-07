# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True
        def balance(node):
            nonlocal result
            if node is None:
                return 0

            left = balance(node.left)
            right = balance(node.right)
            
            if abs(left - right) > 1: 
                result = False

            return max(left,right) + 1
        balance(root)
        return result
        