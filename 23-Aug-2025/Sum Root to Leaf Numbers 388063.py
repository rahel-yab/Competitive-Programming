# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        val = []
        path = []
        def dfs(i):
            path.append(str(i.val))
            if i.left == None and i.right == None:
                val.append(''.join(path))

            if i.left:
                dfs(i.left)
            if i.right:
                dfs(i.right)
            path.pop()

        dfs(root)
        ans = 0
        for i in val:
            ans += int(i)
        return ans
            
            
