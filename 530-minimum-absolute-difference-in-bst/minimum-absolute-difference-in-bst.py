# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minn = float("inf")

        def dfs(node, inorder):
            if not node:
                return
            if node.left:
                dfs(node.left , inorder)
            inorder.append(node.val)
            if node.right:
                dfs(node.right , inorder)
            
            return inorder

        v = dfs(root, [])
        for i in range(1 , len(v)):
            if abs(v[i] - v[i-1]) < minn:
                minn = abs(v[i] - v[i-1])
        
        return minn