# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.check = []
        def isvalidBST(root):
            if root == None: return self.check
            isvalidBST(root.left)
            self.check.append(root.val)
            isvalidBST(root.right)
            return self.check
        t = isvalidBST(root)
        for i in range(1,len(t)):
            if t[i] < t[i-1]: return False
            if i > 0 and t[i] == t[i-1]: return False
        return True
