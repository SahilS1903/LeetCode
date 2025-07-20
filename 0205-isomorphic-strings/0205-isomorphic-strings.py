class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        patterns=[]
        patternt=[]
        for i in range(len(s)):
            patterns.append(s.index(s[i]))
            patternt.append(t.index(t[i]))
            if patterns!=patternt:
                return False
        return True
        