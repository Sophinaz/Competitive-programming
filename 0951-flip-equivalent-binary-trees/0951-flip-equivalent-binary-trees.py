# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            if not root1 and not root2:
                return True
            return False
        
        que = deque([root1])
        que2 = deque([root2])
        track = defaultdict(set)
        track2 = defaultdict(set)

        while que and que2:
            if len(que) != len(que2):
                return False
            for _ in range(len(que)):
                node = que.popleft()
                if node.left:
                    track[node.val].add(node.left.val)
                    que.append(node.left)
                if node.right:
                    track[node.val].add(node.right.val)
                    que.append(node.right)
            for _ in range(len(que2)):
                node = que2.popleft()
                if node.left:
                    track2[node.val].add(node.left.val)
                    que2.append(node.left)
                if node.right:
                    track2[node.val].add(node.right.val)
                    que2.append(node.right)

            for i in track:
                if track[i] != track2[i]:
                    return False
        return True
