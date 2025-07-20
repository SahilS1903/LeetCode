class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # if k>len(nums):
        #     k%=len(nums)

        # for i in range(k):
        #     temp=nums[-1]
            
        #     for j in range(len(nums)-1,0,-1):
                
        #         nums[j]=nums[j-1]
        #     nums[0]=temp

        if k>len(nums):
            k%=len(nums)
        def reverse(arr,start,end):
            while start<end:
                temp=arr[start]
                arr[start]=arr[end]
                arr[end]=temp
                start+=1
                end-=1
            return arr

        reverse(nums,len(nums)-k,len(nums)-1)
        reverse(nums,0,len(nums)-k-1)
        reverse(nums,0,len(nums)-1)