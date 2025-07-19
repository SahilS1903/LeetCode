class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        rev=0
        sign=-1 if x<0 else 1
        x=abs(x)
        while x>0:
            rem=x%10
            x=x//10
            rev=rev*10+rem
        print(rev)
        rev=rev*sign
        if rev>-2**31 and rev<((2**31)-1):
            return rev
        else:
            return 0
        