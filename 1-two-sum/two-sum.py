class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [1 2 3 4 8]
        [0 1 2 3 4]

        [2 3]
        """


        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return [-1, -1]

        # map = {}

        # for i, n in enumerate(nums):
        #     if target - n in map:
        #         return [i, map[target - n]]
        #     map[n] = i
        
        # return [-1, -1]