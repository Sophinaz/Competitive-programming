# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bst(nums):
            if len(nums) == 0: return
            
            n = (len(nums) // 2) 
            node = TreeNode(nums[n])
            
            node.left = bst(nums[:n])
            
            node.right = bst(nums[n+1:])

            return node
                      
        return bst(nums)
