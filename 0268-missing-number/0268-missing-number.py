class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=(len(nums)*(len(nums)+1))/2
        print(sum)
        for i in range(len(nums)):
            sum-=nums[i]
        return sum