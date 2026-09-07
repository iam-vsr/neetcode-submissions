# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt=0
        curr=head
        while(curr):
            cnt+=1
            curr=curr.next
        k=cnt-n+1

        #now delete the Kth element
        if k==1:
            head=head.next
            return head
            
        curr=head
        for _ in range(k-2):
            curr=curr.next
        curr.next=curr.next.next
        return head
        