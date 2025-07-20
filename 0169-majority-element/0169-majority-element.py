class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        n = len(nums)
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > n // 2:
                return num

