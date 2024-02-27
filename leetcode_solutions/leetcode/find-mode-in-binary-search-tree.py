# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.track = defaultdict(int)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def mode(root):    
            if root is None: return

            self.track[root.val] += 1
            mode(root.left)
            mode(root.right)
        
        mode(root)
        
        new = [(i,j) for i,j in self.track.items()]
        new.sort(reverse = True, key=lambda x: x[1])
        result = []
        
        for i in range(len(new)):
            if not result: result.append(new[i][0])
            else: 
                if new[i][1] == new[i-1][1]: result.append(new[i][0])
                else: break
        return result 
            
