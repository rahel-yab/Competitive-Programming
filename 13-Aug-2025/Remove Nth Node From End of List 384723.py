# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        if not head:
            return head
        curr = head
        while curr:
            k += 1
            curr= curr.next
    
    
        val = k - n +1
        if val == 1:
            if head.next:
                head = head.next
            else:
                return None
            return head
        curr2 = head
        prev = None
        count = 0
        while curr2:
            count += 1
            if count == val:
                prev.next = curr2.next
            else:
                prev = curr2
            curr2 = curr2.next
        return head
            