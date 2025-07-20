class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        buy=prices[0]
        for price in prices:
            buy=min(buy,price)
            profit=max(profit,price-buy)

        return profit

