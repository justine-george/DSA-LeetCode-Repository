class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # keep track of running sum map
        # prefix[i] - prefix[j] = k, where i > j, means sum[i:j+1] is k
        
        # first occurence of this sum
        sumMap = {0: -1}

        maxLen = 0
        preSum = 0
        for i, num in enumerate(nums):
            preSum += num

            if preSum - k in sumMap:
                maxLen = max(maxLen, i - sumMap[preSum - k])
            
            if preSum not in sumMap:
                sumMap[preSum] = i
        
        return maxLen