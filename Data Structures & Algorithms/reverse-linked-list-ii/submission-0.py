# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # search start

        headEnd = None
        start = head

        for _ in range(left - 1):
            if not start:
                return head
    
            headEnd = start
            start = start.next
        
        next = start.next
        start.next = None
        curr = start

        for _ in range(right - left):
            temp = next.next
            next.next = curr
            curr = next
            next = temp

        start.next = next

        if headEnd:
            headEnd.next = curr
            return head

        return curr

