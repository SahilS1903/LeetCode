class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h=len(haystack)
        n=len(needle)

        if(h>n or h==n):
            for i in range(h-n+1):
                if needle[0]==haystack[i]:
                    count=1
                    for j in range(1,n):
                        if needle[j]==haystack[i+j]:
                            count+=1
                    if count==len(needle):
                        return i
        
        return -1