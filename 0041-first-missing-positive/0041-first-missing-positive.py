class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            correctPos = nums[i] - 1
            # put num[i] to the correct place if nums[i] in the range [1, n]
            if 0 <= correctPos < n and nums[i] != nums[correctPos]:
                nums[i], nums[correctPos] = nums[correctPos], nums[i]
            else:
                i += 1
        
        # find out the incorrect number
        # first incorrect one would be the first positive missing number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1