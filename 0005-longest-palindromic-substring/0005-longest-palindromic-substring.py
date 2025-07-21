class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n<=1:
            return s
        result=s[0]
        for i in range(1,n+1):
            l,r=i,i
            while l>=0 and r<n and s[l]==s[r]:
                palindrome=s[l:r+1]
                if len(palindrome)>len(result):
                    result=palindrome
                l-=1
                r+=1        
        
            l,r=i-1,i
            while l>=0 and r<n and s[l]==s[r]:
                palindrome=s[l:r+1]
                if len(palindrome)>len(result):
                    result=palindrome
                l-=1
                r+=1  
        return result      