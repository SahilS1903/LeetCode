class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_set=set(nums)
        
        ans=list(sorted(new_set))
        
        for i in range(len(ans)):
            nums[i]=ans[i]
        return len(ans)
        