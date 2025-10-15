class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        ans=''
        for i in range(len(s)):
            if s[i] == '(':
                count+=1
            else:
                count-=1
            if count>1 or (count==1 and s[i]==')' ):
                ans+=s[i]
        return ans