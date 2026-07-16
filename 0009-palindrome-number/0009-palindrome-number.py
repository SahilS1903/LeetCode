class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):return False
        else:
            x=str(x)
            i=0
            j=len(x)-1
            print(i,j)
            while(i<j):
                if x[i]==x[j]:
                    i+=1
                    j-=1
                    continue
                else:
                    return False
            return True
        