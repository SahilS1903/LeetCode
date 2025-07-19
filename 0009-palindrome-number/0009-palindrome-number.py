class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def rev(x):
            rev=0
            
            while x!=0:
                rem=x%10
                x=x//10
                rev=rev*10+rem
            print(rev)
            
            if rev>-2**31 and rev<((2**31)-1):
                return rev
            else:
                return 0
        if x<0:
            return False 
        if x==rev(x):
            return True
        else :
            return False        