class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [1 2 3 4 8]
        [0 1 2 3 4]

        [2 3]
        """

        map = {}
        for i, n in enumerate(nums):
            if target - n in map:
                return [map[target - n], i]
            map[n] = i
        
        return [-1, -1]

        # map = {}

        # for i, n in enumerate(nums):
        #     if target - n in map:
        #         return [i, map[target - n]]
        #     map[n] = i
        
        # return [-1, -1]