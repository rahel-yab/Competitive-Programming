# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_diff = float('-inf')
        def helper(root, cmax,cmin):
            if root == None:
                return float('-inf') , float('inf')
            left_max , left_min= helper(root.left, cmax,cmin)
            right_max ,right_min= helper(root.right, cmax,cmin)
            cmin = min(root.val, left_min, right_min)
            cmax = max(root.val, left_max, right_max)
            self.max_diff = max(self.max_diff, abs(root.val - cmin), abs(root.val- cmax))
            return (cmax , cmin)
        helper(root , float("-inf"), float("inf"))
        return self.max_diff