# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def maxdiff(node,maxx,minn):
            if node is None: 
                return maxx - minn
            
            if node.val < minn: minn = node.val
            if node.val > maxx: maxx = node.val

            return max(maxdiff(node.left,maxx,minn), maxdiff(node.right,maxx,minn))
        return maxdiff(root, float("-inf"), float("inf"))
