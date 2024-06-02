class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # cyclic sort
        # array will contain 1,2,3..n
        i = 0
        while i < n:
            correct_index = nums[i] - 1
            if 0 <= correct_index < n and nums[correct_index] != nums[i]:
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
            else:
                i += 1

        # first improper number's index + 1 is the smallest missing +ve num
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        
        return  n + 1