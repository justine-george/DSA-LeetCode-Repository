class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        globalMax = curMin = curMax = nums[0]

        for num in nums[1:]:
            choices = (num, curMin * num, curMax * num)
            curMin = min(choices)
            curMax = max(choices)
            globalMax = max(globalMax, curMax)
        
        return globalMax