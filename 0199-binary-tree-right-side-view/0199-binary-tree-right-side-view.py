# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None: return result
        que = deque([root])
        while que:
            result.append(que[-1].val)
            for _ in range(len(que)):
                node = que.popleft()
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)   
        return result