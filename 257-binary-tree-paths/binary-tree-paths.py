# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        curr = []

        def backtrack(root):
            if not root:
                return
       
            curr.append(str(root.val))

            if root.left:
                backtrack(root.left)
            if root.right:
                backtrack(root.right)
            
            if not root.left and not root.right:
                paths.append("->".join(curr[:]))
            
            curr.pop()
        
        backtrack(root)
        return paths
