# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        slow.next=None #split the LL into two parts
        first=head

        #reverse the 2nd half
        prev=None
        temp=second
        while temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front

        second=prev #tail becomes the head for the 2nd half

        #merge alternatively
        while second:
            temp1, temp2 = first.next, second.next

            first.next=second
            second.next=temp1
            
            first, second = temp1, temp2
