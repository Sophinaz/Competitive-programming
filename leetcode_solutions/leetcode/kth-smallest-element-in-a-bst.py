# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        def smallest(root):
            if root is None:
                return self.answer
            
            smallest(root.left)
            self.k -= 1
            if self.k == 0: 
                self.answer = root.val
                return self.answer
            smallest(root.right)
            return self.answer
        return smallest(root)