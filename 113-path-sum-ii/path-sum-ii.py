# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans= []
        def dfs(node , path , summ):
            if not node:
                return
            if summ + node.val == targetSum and not node.left and not node.right:
                ans.append(path[:]+[node.val])
                return

            path.append(node.val)
            if node.left:
                dfs(node.left , path , summ+node.val)
            if node.right:
                dfs(node.right , path , summ+node.val)
            path.pop()
        
        dfs(root , [] , 0)
        return ans

