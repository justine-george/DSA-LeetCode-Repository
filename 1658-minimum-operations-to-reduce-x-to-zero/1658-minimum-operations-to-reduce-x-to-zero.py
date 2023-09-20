class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:       
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        
        # we need sliding window to sum upto 'target' and get the min from all the possibilities
        # in other words, find the max window size that sums upto 'target'
        
        curSum = 0
        maxWindow = -1
        l = 0
        for r in range(len(nums)):
            curSum += nums[r]
            
            while l <= r and curSum > target:
                curSum -= nums[l]
                l += 1
                
            if curSum == target:
                maxWindow = max(maxWindow, r - l + 1)
        
        
        return -1 if maxWindow == -1 else len(nums) - maxWindow