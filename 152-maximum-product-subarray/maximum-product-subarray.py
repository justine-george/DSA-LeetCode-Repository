class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        globalMax = curMin = curMax = nums[0]

        for num in nums[1:]:
            curMin, curMax = min(num, curMin * num, curMax * num), max(num, curMin * num, curMax * num)
            globalMax = max(globalMax, curMax)
        
        return globalMax