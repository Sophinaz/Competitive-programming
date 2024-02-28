# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode],level = 0) -> int:
        def diameter(node, val):
            if node is None: return 0
            left = diameter(node.left,val + 1)
            right = diameter(node.right, val + 1 )
            self.answer = max(self.answer, left + right)
            return max(left,right) + 1
        diameter(root,0)
        return self.answer 