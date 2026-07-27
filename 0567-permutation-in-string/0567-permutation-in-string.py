class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def isValid(need, window):
            for key, value in need.items():
                if key not in window or window[key] != value:
                    return False
            return True          # moved out of the for loop

        i, j = 0, 0
        need = {}
        window = {}
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        while j < len(s2):
            window[s2[j]] = window.get(s2[j], 0) + 1

            # shrink first, unconditionally, one step at a time
            while j - i + 1 > len(s1):
                window[s2[i]] -= 1
                if window[s2[i]] == 0:
                    del window[s2[i]]
                i += 1

            if isValid(need, window):
                return True

            j += 1

        return False