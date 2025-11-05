# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
            
        q = deque([root])
        while q:
            curr_level = []
            for _ in range(len(q)):
                curr_node = q.popleft()
                curr_level.append(curr_node)
                if curr_node.left:
                    q.append(curr_node.left)
                    q.append(curr_node.right)
                    
            for i in range(len(curr_level)-1):
                curr_level[i].next = curr_level[i+1]
        
        return root