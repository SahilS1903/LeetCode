class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def isValid(need,window):
            for key,value in need.items():
                if key not in window:
                    return False
                else:
                    if window[key] < value:
                        return False
            return True
        
        i=0
        j=0
        need={}
        window={}
        ans=""
        mini=2**31-1
        for ch in t:
            need[ch]=need.get(ch,0)+1
        while(j<len(s)):
            print(s[j])
            window[s[j]]=window.get(s[j],0)+1
            while isValid(need,window):
                if j-i+1<mini:
                    print(mini)
                    mini=j-i+1
                    ans=s[i:j+1]
                window[s[i]]=window.get(s[i])-1
                i+=1
            j+=1
        return ans
                

        