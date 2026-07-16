class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=0
        output=0
        while(j<len(nums)):
            if nums[j]==1:
                output=max(output,j-i+1)
                j+=1
            else:
                j+=1
                i=j
        return output
            
        