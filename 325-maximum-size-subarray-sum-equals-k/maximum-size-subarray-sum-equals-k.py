class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        maxLen = 0
        preSum = 0
        sumMap = {0: -1}

        for i, num in enumerate(nums):
            preSum += num

            if preSum - k in sumMap:
                maxLen = max(maxLen, i - sumMap[preSum - k])
            
            if preSum not in sumMap:
                sumMap[preSum] = i
        
        return maxLen