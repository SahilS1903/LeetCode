# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        cnt=0
        temp=head
        while temp:
            cnt+=1
            temp=temp.next
        result=cnt-n
        print(result,cnt,n)
        if result==0:
            head=head.next
            return head

        temp=head
        while temp:
            result-=1
            if result==0:
                break
            temp=temp.next
            
        temp.next=temp.next.next
        return head
        

