class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [1 2 3 4 8]
        [0 1 2 3 4]

        [2 3]
        """

        map = {}
        for i in range(len(nums)):
            if target - nums[i] in map:
                return [map[target - nums[i]], i]
            map[nums[i]] = i
        
        return [-1, -1]

        # map = {}

        # for i, n in enumerate(nums):
        #     if target - n in map:
        #         return [i, map[target - n]]
        #     map[n] = i
        
        # return [-1, -1]