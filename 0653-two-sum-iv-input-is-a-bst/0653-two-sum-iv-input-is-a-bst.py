# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        check = defaultdict(int)  
        def bst(node):
            if node is None: return 
            if k - node.val in check:
                return True

            check[node.val] = 1
            return bst(node.left) or bst(node.right)
        return bst(root)
