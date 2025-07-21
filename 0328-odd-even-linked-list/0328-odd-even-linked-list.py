# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head==None or head.next==None:
            return head
        odd=head
        even=odd.next
        evenHead=even
        while even and even.next :
            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        if odd.next:
            odd.next=odd.next.next
        odd.next=evenHead
        return head
