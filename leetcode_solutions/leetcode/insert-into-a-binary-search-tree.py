# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        if root.left == None and val < root.val: 
            root.left = TreeNode(val)
            return root
        elif root.right == None and val >= root.val:
            root.right = TreeNode(val)
            return root
        if val < root.val: 
            self.insertIntoBST(root.left,val)
            return root
        if val >= root.val: 
            self.insertIntoBST(root.right,val)
            return root




