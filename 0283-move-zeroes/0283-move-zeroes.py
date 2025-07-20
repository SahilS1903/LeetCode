class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j=-1
        for i in range(len(nums)):
            if nums[i]==0:
                j=i
                break
        if j==-1:
            return
        for k in range(j+1,len(nums)):
            print(nums[j],nums[k])
            if nums[k]!=0:
                nums[j]=nums[k]
                nums[k]=0
                j+=1

