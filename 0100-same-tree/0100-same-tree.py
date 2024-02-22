# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q or q == None and p:
            self.answer = False
            return self.answer
        if p == None or q == None: return self.answer
        
        if p.val != q.val:
            self.answer = False
            return self.answer
        self.isSameTree(p.left,q.left)
        self.isSameTree(p.right,q.right)
        return self.answer


        