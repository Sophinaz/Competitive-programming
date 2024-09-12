# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0
        def dfs(node):
            nonlocal result
            if node is None: return 0, 0
            later = node.val

            leftx, lefty = dfs(node.left)
            rightx, righty = dfs(node.right)

            numofnodes = lefty + righty + 1
            sumofnodes = leftx + rightx + node.val

            node.val = (sumofnodes) // numofnodes

            if node.val == later: 
                result += 1

            return sumofnodes, numofnodes

        res, num = dfs(root)
        return result