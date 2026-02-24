# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0

        def dfs(root, val ):
            if not root:
                return 

            nonlocal total
            val = 2*val + root.val
            if not root.left and not root.right:
                total += val
                return
        
            dfs(root.left , val )
            dfs(root.right , val)    

        dfs(root , 0)
        return total