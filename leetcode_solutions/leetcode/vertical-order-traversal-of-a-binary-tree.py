# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
        self.track = defaultdict(list)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def vertical(node,col,row):
            if node is None: return
            
            self.track[(col,row)].append(node.val)
            vertical(node.left,col-1,row+1)
            vertical(node.right,col+1,row+1)
        
        vertical(root,0,0)
        track1 = defaultdict(list)
        new = [(i,j) for i,j in self.track.items()]
        new.sort()
        for i,j in new:
            track1[i[0]].extend(sorted(j))
        return [j for _,j in track1.items()]


        
        










