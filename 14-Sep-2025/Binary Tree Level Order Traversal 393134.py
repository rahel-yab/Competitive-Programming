# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = deque([root])
        while q:
            ans.append([node.val for node in q])
            for _ in range(len(q)):
                val = q.popleft()
                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)
        return ans
                