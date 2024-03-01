class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def sortedArray(node):
            if node is None: return
            
            sortedArray(node.left)
            nums.append(node.val)
            sortedArray(node.right)
        
        def balance(path):
            if not path: return
            n = len(path)//2
            node = TreeNode(path[n])
            
            node.left = balance(path[:n])
            node.right = balance(path[n+1:])
            return node
        sortedArray(root)
        return balance(nums)
