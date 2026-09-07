# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        curr=dummy
        carry=0

        while l1!=None or l2!=None:
            summ=carry
            if l1:
                summ+=l1.val
            if l2:
                summ+=l2.val

            new_node=ListNode(summ%10)
            carry=summ//10
            curr.next=new_node
            curr=curr.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        
        if carry:
            curr.next=ListNode(carry)
        
        return dummy.next