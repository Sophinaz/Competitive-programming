# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,node):
        current = node
        while node:
            current = node
            node = node.left
        return current
            
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return
        if val == root.val:
            if not root.left: return root.right
            if not root.right: return root.left
            else: 
                temp = self.inorder(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right,temp.val)
        
        if val < root.val: 
            root.left = self.deleteNode(root.left,val)
        if val >= root.val: 
            root.right = self.deleteNode(root.right,val)
        return root
        