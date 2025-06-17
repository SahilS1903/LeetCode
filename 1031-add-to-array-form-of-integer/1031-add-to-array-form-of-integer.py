class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        # nums=""
        # for i in range(len(num)):
        #     nums=(nums+str(num[i]))
        # nums=str((int(nums))+k)
        # del num
        # ans=[]
        # for i in range(len(nums)):
        #     ans.append(int(nums[i]))
        
        # return ans
        
        res = []
        i = len(num) - 1

        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
            res.append(k % 10)
            k //= 10
            i -= 1

        return res[-1::-1]

