# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        fast=head
        for _ in range(n):
            fast=fast.next
        
        if not fast: # we are asked to delete head
            head=head.next
            return head

        while fast.next:
            slow=slow.next
            fast=fast.next

            if not fast: # we are asked to delete head
                head=head.next
                return head
        
        slow.next=slow.next.next
        return head
        