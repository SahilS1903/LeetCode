class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        for i in range(1,len(nums),2):
            
            for j in range(0,nums[i-1]):
                output.append(nums[i])
        return output        