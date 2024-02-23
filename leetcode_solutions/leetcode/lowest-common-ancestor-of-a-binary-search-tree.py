# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.answer = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None: return self.answer
        if p.val < root.val < q.val or q.val < root.val < p.val:
            self.answer = root
            return self.answer
        if root == p or root == q:
            if not self.answer: self.answer = root
            return self.answer
        self.lowestCommonAncestor(root.left,p,q)
        self.lowestCommonAncestor(root.right,p,q)
        return self.answer
