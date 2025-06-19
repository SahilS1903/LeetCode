# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l=[]
        t=head
        while t:
            l.append(t.val)
            t=t.next
        
        l=l[::-1]
        
        t=head
        for i in range(len(l)):
            t.val=l[i]
            t=t.next
        return head