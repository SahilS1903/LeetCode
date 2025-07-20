class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp={}
        for i in range(len(nums)):
            b=target-nums[i]
            if b in temp:
                return [i,temp[b]]
            else:
                temp[nums[i]]=i
