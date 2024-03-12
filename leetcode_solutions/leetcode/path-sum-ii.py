# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def paths(node, total, path):
            if node is None: return

            if not (node.left or node.right):
                if total + node.val == targetSum:
                    result.append(path[:] + [node.val])
                    return 
            path.append(node.val)
            
            paths(node.left, total + node.val, path)
            paths(node.right, total + node.val, path)
            path.pop()
        
        paths(root, 0, [])
        return result