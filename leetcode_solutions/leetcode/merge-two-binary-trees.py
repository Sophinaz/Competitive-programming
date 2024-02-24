# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode],check=None) -> Optional[TreeNode]:
        if not root1 and not root2: return

        if root1 and root2:
            root2.val = root2.val + root1.val
            root2.left = self.mergeTrees(root1.left, root2.left)
            root2.right = self.mergeTrees(root1.right, root2.right)
            return root2
        if not root1 and root2:
            root2.left = self.mergeTrees(root1, root2.left)
            root2.right = self.mergeTrees(root1, root2.right)
            return root2
        if not root2 and root1:
            root1.left = self.mergeTrees(root1.left, root2)
            root1.right = self.mergeTrees(root1.right, root2)
            return root1 
        
        
        # return root2