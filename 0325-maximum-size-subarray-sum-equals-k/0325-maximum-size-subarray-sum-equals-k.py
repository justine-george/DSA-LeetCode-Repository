class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # we need to keep track of a running sum map
        
        # prefix[i] - prefix[j] = k, where i > j, then sum from i to j is k
        
        # {sum: earliest index for this sum} 
        map = {0: -1}
        
        preSum = 0
        maxLength = 0
        for i in range(len(nums)):
            preSum += nums[i]
            if preSum - k in map:
                maxLength = max(maxLength, i - map[preSum - k])
            if preSum not in map:
                map[preSum] = i
        
        return maxLength