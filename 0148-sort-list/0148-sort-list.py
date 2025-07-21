# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr=list(sorted(arr))
        temp=head
        i=0
        while temp:
            temp.val=arr[i]
            temp=temp.next
            i+=1
        return head