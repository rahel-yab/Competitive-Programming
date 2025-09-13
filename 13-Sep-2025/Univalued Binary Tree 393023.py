# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        val1 = root.val
        while q:
            val2 = q.popleft()
            if val1 != val2.val:
                return False
            
            if val2.left:
                q.append(val2.left)
            if val2.right:
                q.append(val2.right)
        
        return True
