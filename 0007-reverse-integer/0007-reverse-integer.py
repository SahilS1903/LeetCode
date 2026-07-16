class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=1
        if(x>0):
            sign=1
        else:
            sign=-1
        if (sign==-1):
            x*=-1
        print(x) 
        output=0
        while(x>0):
            rem=x%10
            output=output*10+rem
            x/=10
        return sign*output if(-2**31<=output<=2**31-1) else 0
        