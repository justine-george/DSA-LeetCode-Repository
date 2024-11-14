class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            nums[:] = nums[::-1]
            return
        
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        nums[i], nums[j] = nums[j], nums[i]

        nums[i+1:] = nums[i + 1:][::-1]