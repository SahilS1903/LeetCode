class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        k=len(nums)-1
        while(j<=k):
            print(nums,i,j,k)
            if nums[i]==0 and nums[j]==0 and i==j:
                i+=1
                j+=1
            elif(nums[j]==0):
                nums[j]=nums[i]
                nums[i]=0
                i+=1
            elif nums[j]==2:
                nums[j]=nums[k]
                nums[k]=2
                k-=1
            else:
                j+=1
            

        