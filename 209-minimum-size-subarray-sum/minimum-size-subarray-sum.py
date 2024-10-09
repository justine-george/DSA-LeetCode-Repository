class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0 if nums[0] < target else 1
        
        l = r = 0
        min_length = float('inf')
        sum = 0
        while r < len(nums):
            sum += nums[r]

            while sum >= target:
                min_length = min(min_length, r - l + 1)
                sum -= nums[l]
                l += 1

            r += 1
            
        return 0 if min_length == float('inf') else min_length