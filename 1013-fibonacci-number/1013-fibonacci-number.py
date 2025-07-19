class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n if n<=1 else self.fib(n-1)+self.fib(n-2)
