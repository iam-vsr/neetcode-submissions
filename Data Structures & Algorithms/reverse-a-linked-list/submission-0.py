# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        stack=[]
        curr=head
        while curr:
            stack.append(curr)
            curr=curr.next
        
        head=stack.pop()
        curr=head

        while stack:
            curr.next=stack.pop()
            curr=curr.next
        curr.next=None #tail

        return head


        