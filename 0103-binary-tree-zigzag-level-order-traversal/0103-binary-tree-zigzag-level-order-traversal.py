# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        que = deque()
        if root:
            que.append(root)
        idx = 0

        while que:
            temp = []
            for _ in range(len(que)):
                node = que.popleft()
                temp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if not idx:
                result.append(temp)
            else:
                result.append(temp[::-1])
            idx = 1 - idx
        return result