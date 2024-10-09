class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0 if nums[0] < target else 1
        
        l = r = 0
        min_length = float('inf')
        sum = 0
        while r < len(nums):
            while r < len(nums) and sum < target:
                sum += nums[r]
                r += 1

            while sum >= target:
                min_length = min(min_length, r - l)
                sum -= nums[l]
                l += 1
            
        return 0 if min_length == float('inf') else min_length