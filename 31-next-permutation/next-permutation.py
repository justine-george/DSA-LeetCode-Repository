class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find first i from right less than i + 1
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            nums[:] = nums[::-1]
            return
        # found i

        # find first number starting from end, greater than i
        j = len(nums) - 1
        while j > i and nums[i] >= nums[j]:
            j -= 1
        # found j

        # swap i and j
        nums[i], nums[j] = nums[j], nums[i]

        # reverse i + 1 and beyond to get next smallest
        nums[i+1:] = nums[i+1:][::-1]