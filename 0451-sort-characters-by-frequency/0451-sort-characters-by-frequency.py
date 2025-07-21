class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        # Sort unique characters by frequency
        sorted_chars = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        result = ''
        for char, count in sorted_chars:
            result += char * count

        return result



        