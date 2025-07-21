class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        ans=0
        for i in range(len(s)-1,0,-1):
            value1=roman_dict[s[i]]
            
            value2=roman_dict[s[i-1]]
            
            if value1>value2:
                ans=ans+value1-2*value2
            else :
                ans+=value1
            
        ans+=roman_dict[s[0]]
        return(ans)

        