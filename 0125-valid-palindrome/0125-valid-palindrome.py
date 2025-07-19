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




class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()

        # Clean the string in-place
        def is_alnum(c):
            return c.isalnum()

        def recurse(i, j):
            # Base case: pointers crossed
            if i >= j:
                return True
            # Skip non-alphanumeric characters
            if not is_alnum(s[i]):
                return recurse(i + 1, j)
            if not is_alnum(s[j]):
                return recurse(i, j - 1)
            # Check mismatch
            if s[i] != s[j]:
                return False
            return recurse(i + 1, j - 1)

        return recurse(0, len(s) - 1)
