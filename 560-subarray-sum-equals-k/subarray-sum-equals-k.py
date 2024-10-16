class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0: 1}
        res_count = 0
        preSum = 0
        for r in range(len(nums)):
            preSum += nums[r]

            if preSum - k in map:
                res_count += map[preSum - k]
            
            map[preSum] = map.get(preSum, 0) + 1
        
        return res_count