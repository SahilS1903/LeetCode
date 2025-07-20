class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # cnt0=0
        # cnt1=0
        # cnt2=0
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         cnt0+=1
        #     if nums[i]==1:
        #         cnt1+=1
        #     if nums[i]==2:
        #         cnt2+=1
        # print(cnt0,cnt1,cnt2)
        # for i in range(cnt0):
        #     nums[i]=0
        # for i in range(cnt0,cnt1+cnt0):
        #     nums[i]=1
        # for i in range(cnt1+cnt0,cnt1+cnt0+cnt2):
        #     nums[i]=2

        low=0
        mid=0
        high=len(nums)-1

        while(mid<=high):
            if nums[mid]==0:
                temp=nums[low]
                nums[low]=nums[mid]
                nums[mid]=temp
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                temp=nums[high]
                nums[high]=nums[mid]
                nums[mid]=temp
                high-=1
