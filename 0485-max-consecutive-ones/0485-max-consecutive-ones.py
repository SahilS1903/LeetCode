class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                maximum=max(maximum,count)
            else:
                count=0

        return maximum