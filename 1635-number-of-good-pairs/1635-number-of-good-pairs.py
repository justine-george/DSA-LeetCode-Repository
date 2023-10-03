class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        map = {}
        res = 0
        for i in range(len(nums)):
            if nums[i] in map:
                res += len(map[nums[i]])
                map[nums[i]].append(i)
            else:
                map[nums[i]] = [i]
        
        return res

        # [1,2,3,1,1,3]
        #  0 1 2 3 4 5

        # map = {
        #     1: [0, 3, 4]
        #     2: [1]
        #     3: [2]

        # }

        # res = 1 + 2 + 1