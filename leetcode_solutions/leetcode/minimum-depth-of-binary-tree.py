# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def minimum(node):
            if node is None: return float('inf')
            if not node.left and not node.right:
                return 1

            left = minimum(node.left)
            right = minimum(node.right)

            return min(left,right) + 1
        result = minimum(root)
        
        if result == float('inf'): return 0
        else: return result