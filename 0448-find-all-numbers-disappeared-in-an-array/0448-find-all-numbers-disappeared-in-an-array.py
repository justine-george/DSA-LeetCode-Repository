class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Initialization
        res = []
        
        # Cyclic sort
        i = 0
        while i < len(nums):
            correctPos = nums[i] - 1
            # if the number is not at its correct position
            if nums[i] != nums[correctPos]:
                nums[i], nums[correctPos] = nums[correctPos], nums[i]
            else:
                i += 1
                
        # Go through every element
        # If nums[i] != i + 1, (i + 1) is the disappeared num
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)
        
        return res