# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root,p,q):
            if root == None:
                return None
            if q.val > root.val and p.val > root.val:
                return helper(root.right,p,q)
            if q.val < root.val and p.val < root.val:
                return helper(root.left,p,q)
            return root
        return helper(root,q,p)