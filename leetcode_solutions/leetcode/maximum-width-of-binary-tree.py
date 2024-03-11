# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:   
        track = {}
        def width(node, lev, col):
            if node is None: return

            if lev in track:
                if col < track[lev][0]:
                    track[lev][0] = col
                if col > track[lev][1]:
                    track[lev][1] = col
            else:
                track[lev] = [col,col]

            width(node.left, lev+1, (2*col) - 1)
            width(node.right, lev+1, (2*col))
        
        width(root, 0, 1)
        result = 0
        for i in track:
            result = max(result, track[i][1] - track[i][0] + 1)
        
        return result 

