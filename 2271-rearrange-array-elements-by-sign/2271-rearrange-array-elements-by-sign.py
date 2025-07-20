class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        ans=[0]*l
        positiveInd=0
        negativeInd=1
        for num in nums:
            
            if num>0:
                ans[positiveInd]=num
                positiveInd+=2
            else:
                ans[negativeInd]=num
                negativeInd+=2
        return ans