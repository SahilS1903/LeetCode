class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        for i in range(len(strs[0])):
            key=strs[0][:i+1]
            print(key)
            for j in range(1,len(strs)):
                if key!=strs[j][:i+1]:
                    return strs[0][:i]
            
        return strs[0]

        