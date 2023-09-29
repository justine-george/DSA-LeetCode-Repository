class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # T: O(n), S: O(1)
        # 4 steps:

        # step1
        # find a number < than its right
        i = len(nums) - 1
        while i >= 1 and nums[i - 1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums[:] = nums[::-1]
            return
        
        # now i - 1 is the index we need

        # step2
        # find the 1st number from right > than nums[i - 1]
        j = len(nums) - 1
        while j > i - 1 and nums[j] <= nums[i - 1]: 
            j -= 1

        # now j is the index we need

        # step3
        # swap numbers at i - 1 and j
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # step4
        # to sort numbers from i to the end, we only need to reverse that part
        nums[i:] = nums[i:][::-1]