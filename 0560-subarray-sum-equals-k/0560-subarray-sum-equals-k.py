class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dict={}
        dict[0]=1
        preSum=0
        cnt=0
        for num in nums:
            preSum+=num
            diff=preSum-k
            if diff in dict:
                cnt+=dict[diff]
            dict[preSum] = dict.get(preSum, 0) + 1
        return cnt
