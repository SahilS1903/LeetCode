class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev=''
        s=s.strip()
        i=0
        while i<len(s):
            if s[i]==" ":
                rev=' '+s[:i]+rev
                s=s[i+1:].strip()
                i=0
            i+=1
        rev=s+rev
        return rev