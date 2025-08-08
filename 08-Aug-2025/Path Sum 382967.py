# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(i, targetSum):
            if not i:
                return False
            targetSum -= i.val
            if not i.left and not i.right:
                return targetSum  == 0
            
            return dfs(i.right,targetSum ) or dfs(i.left,targetSum)
        
        return dfs(root, targetSum)

