class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            a=nums[i]
            b=target-a
            for j in range(i+1,len(nums)):
                if b == nums[j]:
                    return [i,j]
        return []