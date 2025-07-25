# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # slow=head
        # fast=head
        # while fast and fast.next!=None :
        #     fast=fast.next.next
        #     slow=slow.next
        #     if fast==slow:
        #         return True
        # return False

        dict={}
        temp=head
        while temp:
            if temp in dict:
                return True
            dict[temp]=1
            temp=temp.next
        return False
        
        