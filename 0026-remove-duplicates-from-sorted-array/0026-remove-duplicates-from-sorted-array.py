class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1 : 
            return 1
        ans=[]
        ans.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                
                ans.append(nums[i])
                
        for i in range(len(ans)):
            nums[i]=ans[i]
        return len(ans)
            
        