# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def backtrack(nums):
            if not nums: return
            
            n = nums.index(max(nums))
            node = TreeNode(nums[n])

            node.left = backtrack(nums[:n])
            node.right = backtrack(nums[n+1:])
            return node
        return backtrack(nums)