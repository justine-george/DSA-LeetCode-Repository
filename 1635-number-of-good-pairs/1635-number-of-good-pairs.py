class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        map = {}
        res = 0
        for i in range(len(nums)):
            # every element that already exists helps make a new pair
            res += map.get(nums[i], 0)
            map[nums[i]] = map.get(nums[i], 0) + 1
        
        return res