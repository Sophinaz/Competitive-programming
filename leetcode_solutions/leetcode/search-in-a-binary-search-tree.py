# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self): self.answer = None
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None: return

        if val < root.val: self.searchBST(root.left,val)
        elif val > root.val: self.searchBST(root.right,val)
        else:
            self.answer = root 
            return self.answer
        return self.answer