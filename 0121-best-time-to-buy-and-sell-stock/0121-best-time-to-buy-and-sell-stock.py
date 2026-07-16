class Solution(object):
    def maxProfit(self, nums):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini=nums[0]
        profit=0
        for num in nums:
            profit=max(profit,num-mini)
            mini=min(num,mini)
        return profit

        