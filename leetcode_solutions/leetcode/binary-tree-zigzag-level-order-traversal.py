# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = []
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def zigzag(node,level):
            if node is None: return

            if level < len(self.answer): self.answer[level].append(node.val)               
            else: self.answer.append([node.val])

            zigzag(node.left,level+1)
            zigzag(node.right,level+1)
        zigzag(root,0)
        for i in range(len(self.answer)):
            if i % 2: self.answer[i] = self.answer[i][::-1]
        return self.answer
        
