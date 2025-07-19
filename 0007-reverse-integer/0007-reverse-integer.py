class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            reversed_int=int(str(x)[::-1]) 
        else:
            reversed_int=-int(str(-x)[::-1])
        
        if -2**31 <= reversed_int <= (2**31) - 1:
            return reversed_int
        else :
            return 0
        
        
        
       

        


        