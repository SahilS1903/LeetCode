class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(arr, i, j):
            while j > i:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        # Step 1: Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If such element was found, find the next bigger element and swap
        if i >= 0:
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break

        # Step 3: Reverse the tail part
        reverse(nums, i + 1, len(nums) - 1)
