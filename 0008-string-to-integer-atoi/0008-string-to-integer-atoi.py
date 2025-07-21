class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        s=s.strip()
        sign=1
        if not s:
            return 0
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        
        result=0
        while i<len(s) :
            if s[i].isdigit():
                result=result*10+int(s[i])
                i+=1
            else:
                break
        result*=sign
        
        if result>(2**31)-1 :
            
            return 2**31 -1
        if result<-2**31:
            
            return -2**31 
        
        else:
            
            return result