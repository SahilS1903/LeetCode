class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        for i in range(len(nums)):
            if cnt==0:
                el=nums[i]
                cnt+=1
            elif nums[i]==el:
                cnt+=1
            else:
                cnt-=1
        return el