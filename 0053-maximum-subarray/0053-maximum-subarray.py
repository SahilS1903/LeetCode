class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=-2**31
        sum=0
        for num in nums:
            sum+=num
            if(sum>maxi):
                maxi=sum
            if sum<0:
                sum=0
            
        return maxi

