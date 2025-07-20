class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        opened = 0

        for c in s:
            
            if c == '(':
                if opened > 0:
                    result.append(c)
                opened += 1
            elif c == ')':
                opened -= 1
                if opened > 0:
                    result.append(c)

        return ''.join(result)
        