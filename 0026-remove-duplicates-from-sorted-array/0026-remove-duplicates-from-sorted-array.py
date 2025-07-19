# class Solution(object):
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     new_set=set(nums)
        
    #     ans=list(sorted(new_set))
        
    #     for i in range(len(ans)):
    #         nums[i]=ans[i]
    #     return len(ans)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        for j in range (1,len(nums)):
            if nums[j]>nums[i]:
                nums[i+1]=nums[j]
                i+=1
        return i+1
