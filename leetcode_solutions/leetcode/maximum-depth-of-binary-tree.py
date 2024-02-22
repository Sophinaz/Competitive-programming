# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
        self.curr = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None: 
            self.result = max(self.result,self.curr)
            return self.result

        self.curr += 1 
        self.maxDepth(root.left)
        self.maxDepth(root.right)
        self.curr -= 1
        return self.result
