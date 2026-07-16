class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp=0
        for i in range(len(nums)):
            if nums[i]<=nums[(i+1)%len(nums)]:
                continue
            else:temp+=1
        return True if temp<=1 else False
        