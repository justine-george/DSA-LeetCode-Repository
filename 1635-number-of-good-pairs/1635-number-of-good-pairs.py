class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        map = {}
        res = 0
        for i in range(len(nums)):
            res += map.get(nums[i], 0)
            map[nums[i]] = map.get(nums[i], 0) + 1
        
        return res