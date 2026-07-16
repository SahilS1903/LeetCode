class Solution(object):
    def rotatearr(self,nums,i,j):
        while(i<j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            i+=1
            j-=1
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n=len(nums)
        k=k%n
        self.rotatearr(nums,0,n-k-1)
        self.rotatearr(nums,n-k,n-1)
        self.rotatearr(nums,0,n-1)
    
        