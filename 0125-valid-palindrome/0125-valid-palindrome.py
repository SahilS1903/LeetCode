class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned=''
        s=s.lower()
        for i in range (len(s)):
            if s[i].isalnum():
                cleaned+=s[i]
        print(cleaned)
        return self.palindrome(0,cleaned)

    def palindrome(self,j,p):
        if j>=len(p):
            return True
        if p[j]!=p[len(p)-j-1]:
            return False
        return self.palindrome(j+1,p) 
