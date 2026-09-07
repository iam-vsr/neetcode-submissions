# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        dummy_head=ListNode(-1)
        dummy=dummy_head

        while curr1 and curr2:
            if curr1.val>curr2.val:
                dummy.next=curr2
                curr2=curr2.next
                dummy=dummy.next
            else:
                dummy.next=curr1
                curr1=curr1.next
                dummy=dummy.next
        
        while curr1:
            dummy.next=curr1
            curr1=curr1.next
            dummy=dummy.next
        
        while curr2:
            dummy.next=curr2
            curr2=curr2.next
            dummy=dummy.next
        
        return dummy_head.next

        