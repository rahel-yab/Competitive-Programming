# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        height = 0
        if not root:
            return 0
        
        height = 0
        curr = root
        while curr:
            height += 1
            curr = curr.left


        def check(mid, root, right):
            if not root:
                return False
        
            if right == 1:
                return root is not None
        
            pivot = right // 2
            if mid < pivot:
                return check(mid, root.left, pivot)
            else:
                return check(mid - pivot, root.right, pivot)

        low = 0
        val = 2**(height -1) 
        high = val

        while low < high:
            mid = (low+high) // 2
            if check(mid , root, val):
                low = mid + 1
            else:
                high = mid 

        return 2**(height-1) -1 + low