# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dict={}
        temp=head
        while temp:
            if temp in dict:
                return temp
            dict[temp]=1
            temp=temp.next
        return None
        