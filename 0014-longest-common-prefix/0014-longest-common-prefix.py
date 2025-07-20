# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         for i in range(len(strs[0])):                  # loop through each character index of the first string
#             key = strs[0][:i+1]                         # take prefix of length (i+1) from the first string
#             print(key)                                  # print current prefix (for debugging)
#             for j in range(1, len(strs)):               # loop over the rest of the strings
#                 if key != strs[j][:i+1]:                # if the prefix doesn’t match in any string
#                     return strs[0][:i]                  # return the prefix up to index i (excluding current character)
#         return strs[0]                                  # if full first string is prefix, return it




class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i in range(len(strs[0])):             # loop over each character index in the first string
            char = strs[0][i]                     # take the i-th character
            for s in strs[1:]:                    # check this char against all other strings
                if i >= len(s) or s[i] != char:   # mismatch or string is shorter
                    return strs[0][:i]            # return common prefix up to i
        return strs[0]                            # all characters matched

